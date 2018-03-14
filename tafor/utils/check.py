import re
import datetime

from PyQt5.QtCore import QObject

from tafor import conf, logger
from tafor.models import db, Taf, Metar
from tafor.states import context

from tafor.utils.validator import Grammar


def formatTimez(message):
    try:
        m = Grammar.timez.search(message).groups()
        utc =  datetime.datetime.utcnow()
        created = datetime.datetime(utc.year, utc.month, int(m[0]), int(m[1]), int(m[2]))
        return created
    except Exception as e:
        logger.error(e, exc_info=True)
        created = datetime.datetime.utcnow()
        return created


class CheckTaf(QObject):
    """docstring for CheckTaf"""
    def __init__(self, tt, message=None, time=None, prev=0):
        super(CheckTaf, self).__init__()
        self.tt = tt
        self.message = message
        self.time = datetime.datetime.utcnow() if time is None else time

        interval = {
            'FC': 3,
            'FT': 6,
        }

        self.interval = interval.get(self.tt)

        if prev:
            self.time -= datetime.timedelta(hours=self.interval * prev)

        startOfTheDay = datetime.datetime(self.time.year, self.time.month, self.time.day)
        startTime = dict()
        startTime['FC'] = {
                    '0312': startOfTheDay + datetime.timedelta(hours=1),
                    '0615': startOfTheDay + datetime.timedelta(hours=4),
                    '0918': startOfTheDay + datetime.timedelta(hours=7),
                    '1221': startOfTheDay + datetime.timedelta(hours=10),
                    '1524': startOfTheDay + datetime.timedelta(hours=13),
                    '1803': startOfTheDay + datetime.timedelta(hours=16),
                    '2106': startOfTheDay + datetime.timedelta(hours=19),
                    '0009': startOfTheDay + datetime.timedelta(hours=22),
        }
        startTime['FT'] = {
                    '0606': startOfTheDay + datetime.timedelta(hours=1),
                    '1212': startOfTheDay + datetime.timedelta(hours=7),
                    '1818': startOfTheDay + datetime.timedelta(hours=13),
                    '0024': startOfTheDay + datetime.timedelta(hours=19),
        }

        if self.time < startOfTheDay + datetime.timedelta(hours=1):
            startTime['FC']['0009'] -= datetime.timedelta(days=1)
            startTime['FT']['0024'] -= datetime.timedelta(days=1)

        endTimeDelta = {
            'FC': {
                'normal': datetime.timedelta(minutes=50),
                'warning': datetime.timedelta(hours=3),
            },
            'FT': {
                'normal': datetime.timedelta(hours=2, minutes=50),
                'warning': datetime.timedelta(hours=6),
            }
        }

        # 00 - 01 时次特殊情况
        defaultPeriod = {
            'FC': '0009', 
            'FT': '0024',
        }

        self.startTime = startTime.get(self.tt)
        self.endTimeDelta = endTimeDelta.get(self.tt)
        self.defaultPeriod = defaultPeriod.get(self.tt)

    def normalPeriod(self, withDay=True):
        period = self._findPeriod(self.endTimeDelta['normal'])

        if withDay:
            return self._withDay(period)

        return period

    def warningPeriod(self, withDay=True):
        period = self._findPeriod(self.endTimeDelta['warning'], self.defaultPeriod)

        if withDay:
            return self._withDay(period)

        return period

    def local(self, period=None):
        period = self.warningPeriod() if period is None else period
        expired = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
        recent = db.query(Taf).filter(Taf.rpt.contains(period), Taf.sent > expired).order_by(Taf.sent.desc()).first()
        return recent

    def remote(self):
        if self.message:
            match = Grammar.period.search(self.message)
            if match and match.group() == self.warningPeriod():
                return self.message

        return None

    def save(self, callback=None):
        last = db.query(Taf).filter_by(tt=self.tt).order_by(Taf.sent.desc()).first()

        if last is None or last.rptInline != self.message:  # 如果数据表为空 或 最后一条数据和远程不相等
            item = Taf(tt=self.tt, rpt=self.message, confirmed=self.time)
            db.add(item)
            db.commit()
            logger.info('Save {} {}'.format(self.tt, self.message))

            if callback:
                callback()

    def confirm(self, callback=None):
        last = db.query(Taf).filter_by(tt=self.tt).order_by(Taf.sent.desc()).first()

        if last is not None and last.rptInline == self.message:
            last.confirmed = self.time
            db.commit()
            logger.info('Confirm {} {}'.format(self.tt, self.message))

            if callback:
                callback()

    def hasExpired(self, offset=None):
        offset = offset or conf.value('Monitor/WarnTAFTime')
        offset = int(offset) if offset else 30
        offsetTimeDelta = {
            'FC': datetime.timedelta(minutes=offset), 
            'FT': datetime.timedelta(hours=2, minutes=offset)
        }

        timedelta = offsetTimeDelta.get(self.tt)
        period = self.warningPeriod(withDay=False)
        start = self.startTime.get(period)

        threshold = start + timedelta
        return threshold < self.time

    def _findPeriod(self, endTimeDelta, default=None):
        for period, start in self.startTime.items():
            if start <= self.time <= start + endTimeDelta:
                return period

        if default:
            return default

    def _withDay(self, period):
        if period is None:
            return None
        
        time = self.time

        # 跨越 UTC 日界
        if period in ('0009', '0024') and self.time.hour != 0:
            time = self.time + datetime.timedelta(days=1)

        periodWithDay = str(time.day).zfill(2) + period

        return periodWithDay


class CheckMetar(object):
    """docstring for CheckMetar"""
    def __init__(self, tt, message):
        self.tt = tt
        self.message = message

    def save(self):
        last = db.query(Metar).filter_by(tt=self.tt).order_by(Metar.created.desc()).first()
        
        if last is None or last.rpt != self.message:
            item = Metar(tt=self.tt, rpt=self.message, created=formatTimez(self.message))
            db.add(item)
            db.commit()
            logger.info('Save {} {}'.format(self.tt, self.message))


class Listen(object):

    def __init__(self, parent=None):
        self.parent = parent

    def __call__(self, tt):
        self.tt = tt
        state = context.message.state()
        self.message = state.get(self.tt, None)
        method = {'FC': 'taf', 'FT': 'taf', 'SA': 'metar', 'SP': 'metar'}
        return getattr(self.__class__, method[self.tt])(self)

    def taf(self):

        def afterSave():
            self.parent.notificationSound.play(loop=False)
            self.parent.alarmMessageBox.close()

        expired = False

        taf = CheckTaf(self.tt, message=self.message)
        local = taf.local()

        if local:
            if not local.confirmed:
                if taf.remote():
                    taf.confirm(callback=afterSave)
                elif taf.hasExpired():
                    expired = True
        else:
            if taf.remote():
                taf.save(callback=afterSave)
            elif taf.hasExpired():
                expired = True

        context.taf.setState({
            taf.tt: {
                'period': taf.warningPeriod(),
                'sent': True if local else False,
                'warnning': expired,
                'clock': taf.hasExpired(offset=5),
            }
        })

    def metar(self):
        metar = CheckMetar(self.tt, message=self.message)
        if self.message:
            metar.save()

