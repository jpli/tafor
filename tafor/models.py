import os
import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from tafor import BASEDIR


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'db.sqlite3')

Base = declarative_base()

class Taf(Base):
    __tablename__ = 'tafs'
    
    id = Column(Integer, primary_key=True)
    tt = Column(String(2))
    sign = Column(String(255), nullable=True)
    rpt = Column(String(255))
    raw = Column(String(255), nullable=True)
    sent = Column(DateTime, default=datetime.datetime.utcnow)
    confirmed = Column(DateTime, nullable=True)

    # task = relationship('tasks', lazy='dynamic')

    def __init__(self, tt, rpt, sign=None, raw=None, confirmed=None):
        self.tt = tt
        self.sign = sign
        self.rpt = rpt
        self.raw = raw
        self.confirmed = confirmed

    def __repr__(self):
        return '<TAF %r %r>' % (self.tt, self.rpt)

    @property
    def rptInline(self):
        return self.rpt.replace('\n', ' ')

    @property
    def report(self):
        from tafor.utils import Parser
        rpt = Parser(self.rpt)
        parts = [self.sign, rpt.renderer()]
        return '\n'.join(filter(None, parts))

class Metar(Base):
    __tablename__ = 'metars'

    id = Column(Integer, primary_key=True)
    tt = Column(String(2))
    rpt = Column(String(255))
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, tt, rpt):
        self.tt = tt
        self.rpt = rpt

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    tt = Column(String(2))
    sign = Column(String(255))
    rpt = Column(String(255))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    planning = Column(DateTime)

    taf_id = Column(Integer, ForeignKey('tafs.id'))

    def __init__(self, tt, sign, rpt, planning):
        self.tt = tt
        self.sign = sign
        self.rpt = rpt
        self.planning = planning

    def __repr__(self):
        return '<Task TAF %r %r %r>' % (self.tt, self.rpt, self.planning)

class Trend(Base):
    __tablename__ = 'trends'

    id = Column(Integer, primary_key=True)
    sign = Column(String(16))
    rpt = Column(String(255))
    raw = Column(String(255))
    sent = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, sign, rpt, raw=None):
        self.sign = sign
        self.rpt = rpt
        self.raw = raw

    def __repr__(self):
        return '<Trend %r>' % (self.rpt)

    @property
    def tt(self):
        return 'TREND'

    @property
    def report(self):
        return self.rpt

    def isNosig(self):
        return self.rpt == 'NOSIG='

class Sigmet(Base):
    __tablename__ = 'sigmets'

    id = Column(Integer, primary_key=True)
    tt = Column(String(2))
    sign = Column(String(255))
    rpt = Column(String(255))
    raw = Column(String(255))
    sent = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, tt, sign, rpt, raw=None):
        self.tt = tt
        self.sign = sign
        self.rpt = rpt
        self.raw = raw

    def __repr__(self):
        return '<Sigmet %r %r>' % (self.tt, self.rpt)

    @property
    def report(self):
        parts = [self.sign, self.rpt]
        return '\n'.join(filter(None, parts))

    def isCnl(self):
        return 'CNL' in self.rpt

    def expire(self):
        import re
        from tafor.utils.convert import parseDateTime
        pattern = re.compile(r'(\d{6})/(\d{6})')
        endingTime = pattern.search(self.rpt).group(2)
        return parseDateTime(endingTime, self.sent)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(8))
    mobile = Column(String(20))

    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    def __repr__(self):
        return '<User %r %r>' % (self.name, self.mobile)



engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Session = sessionmaker(bind=engine)
db = Session()

Base.metadata.create_all(engine)