import os
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtNetwork import QLocalSocket, QLocalServer
from PyQt5.QtMultimedia import QSound, QSoundEffect

from tafor import BASEDIR, conf, logger, boolean, __version__
from tafor.models import db, Tafor, Task, Metar, User
from tafor.utils import Listen, checkVersion
from tafor.utils.thread import WorkThread, CallThread, CheckUpgradeThread

from tafor.components.ui import Ui_main, main_rc
from tafor.components.taf import TAFEditor, TaskTAFEditor
from tafor.components.trend import TrendEditor
from tafor.components.sigmet import SigmetEditor
from tafor.components.send import TaskTAFSender, TAFSender, TrendSender, SigmetSender
from tafor.components.setting import SettingDialog
from tafor.components.task import TaskBrowser

from tafor.components.widgets.widget import createAlarmMsgBox, Clock, CurrentTAF, RecentTAF
from tafor.components.widgets.status import WebAPIStatus, CallServiceStatus
from tafor.components.widgets.sound import Sound


class Context(QtCore.QObject):
    warningSignal = QtCore.pyqtSignal()
    reminderSignal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(Context, self).__init__()
        self._message = {}
        self._callService = None
        self._warning = {
            'FC': False,
            'FT': False
        }
        self._current = {
            'FC': {
                'period': '',
                'status': False
            },
            'FT': {
                'period': '',
                'status': False
            }
        }
        self._reminder = {
            'FC': False,
            'FT': False
        }

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg

    @property
    def webApi(self):
        return True if self._message else False

    @property
    def callService(self):
        return self._callService

    @callService.setter
    def callService(self, value):
        self._callService = value

    @property
    def warning(self):
        return self._warning

    @warning.setter
    def warning(self, values):
        try:
            tt, hasExpired = values
            self._warning[tt] = hasExpired
            self.warningSignal.emit()
        except ValueError:
            raise ValueError

    def isWarning(self):
        return any(self._warning.values())

    @property
    def reminder(self):
        return self._reminder

    @reminder.setter
    def reminder(self, values):
        try:
            tt, hasExpired = values
            if self._reminder[tt] != hasExpired:
                self._reminder[tt] = hasExpired
                self.reminderSignal.emit(tt)
        except ValueError:
            raise ValueError

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, values):
        try:
            tt, period, status = values
            current = self._current[tt]
            current['period'] = period
            current['status'] = status
        except ValueError:
            raise ValueError
        

class MainWindow(QtWidgets.QMainWindow, Ui_main.Ui_MainWindow):
    """
    主窗口
    """
    def __init__(self, parent=None):
        """
        初始化主窗口
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.context = Context()
        self.context.warningSignal.connect(self.dialer)
        self.context.reminderSignal.connect(self.reminder)

        # 初始化剪贴板
        self.clip = QtWidgets.QApplication.clipboard()

        # 初始化窗口
        self.taskBrowser = TaskBrowser(self)
        self.settingDialog = SettingDialog(self)

        self.tafSender = TAFSender(self)
        self.taskTAFSender = TaskTAFSender(self)
        self.trendSender = TrendSender(self)
        self.sigmetSender = SigmetSender(self)

        self.tafEditor = TAFEditor(self, self.tafSender)
        self.taskTAFEditor = TaskTAFEditor(self, self.taskTAFSender)
        self.trendEditor = TrendEditor(self, self.trendSender)
        self.sigmetEditor = SigmetEditor(self, self.sigmetSender)

        # 设置主窗口文字图标
        self.setWindowIcon(QtGui.QIcon(':/logo.png'))

        self.setupRecent()

        # 设置切换联系人菜单
        self.setupContractMenu()

        # 设置系统托盘
        self.setupSysTray()

        self.setupStatusBar()

        self.setupThread()

        self.setupSound()

        # 连接菜单信号
        self.tafAction.triggered.connect(self.tafEditor.show)
        self.trendAction.triggered.connect(self.trendEditor.show)
        self.sigmetAction.triggered.connect(self.sigmetEditor.show)

        # 添加定时任务菜单
        # self.taskTafAction = QtWidgets.QAction(self)
        # self.post_menu.addAction(self.taskTafAction)
        # self.taskTafAction.setText('定时任务')
        # self.taskTafAction.triggered.connect(self.taskTAFEditor.show)

        # 连接设置对话框的槽
        self.settingAction.triggered.connect(self.settingDialog.exec_)
        self.settingAction.triggered.connect(self.showWindow)
        self.settingAction.setIcon(QtGui.QIcon(':/setting.png'))

        self.reportIssueAction.triggered.connect(self.reportIssue)
        self.checkUpgradeAction.triggered.connect(self.checkUpgradeThread.start)

        # 连接关于信息的槽
        self.aboutAction.triggered.connect(self.about)
        self.aboutAction.triggered.connect(self.showWindow)

        # 连接切换联系人的槽
        self.contractsActionGroup.triggered.connect(self.changeContract)
        self.contractsActionGroup.triggered.connect(self.settingDialog.load)

        # 连接报文表格复制的槽
        self.tafTable.itemDoubleClicked.connect(self.copySelectItem)
        self.metarTable.itemDoubleClicked.connect(self.copySelectItem)

        # 时钟计时器
        self.clockTimer = QtCore.QTimer()
        self.clockTimer.timeout.connect(self.singer)
        self.clockTimer.start(1 * 1000)

        self.workerTimer = QtCore.QTimer()
        self.workerTimer.timeout.connect(self.worker)
        self.workerTimer.start(60 * 1000)

        self.updateGUI()
        self.worker()

    def setupRecent(self):
        self.clock = Clock(self, self.tipsLayout)
        self.tipsLayout.addSpacerItem(QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        self.currentTAF = CurrentTAF(self, self.tipsLayout)
        self.recentFT = RecentTAF(self, self.recentLayout, 'FT')
        self.recentFC = RecentTAF(self, self.recentLayout, 'FC')

    def setupContractMenu(self):
        self.contractsActionGroup = QtWidgets.QActionGroup(self)
        self.contractsActionGroup.addAction(self.contractNo)
        
        contacts = db.query(User).all()

        for person in contacts:
            setattr(self, 'contract' + str(person.id), QtWidgets.QAction(self))
            target = getattr(self, 'contract' + str(person.id))
            target.setText(person.name)
            target.setCheckable(True)

            self.contractsActionGroup.addAction(target)
            self.contractsMenu.addAction(target)

        self.updateContractMenu()

    def setupSysTray(self):
        # 设置系统托盘
        self.tray = QtWidgets.QSystemTrayIcon(self)
        self.tray.setIcon(QtGui.QIcon(':/logo.png'))
        self.tray.show()

        # 连接系统托盘的槽
        self.tray.activated.connect(self.restoreWindow)

        self.trayMenu = QtWidgets.QMenu(self)

        self.trayMenu.addAction(self.contractsMenu.menuAction())
        self.trayMenu.addAction(self.settingAction)
        self.trayMenu.addAction(self.aboutAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(self.quitAction)

        self.tray.setContextMenu(self.trayMenu)

        message = '预报发报软件 v' + __version__
        self.tray.setToolTip(message)

    def setupStatusBar(self):
        self.webApiStatus = WebAPIStatus(self, self.statusBar)
        self.callServiceStatus = CallServiceStatus(self, self.statusBar, last=True)

        # self.statusBar.setStyleSheet('QStatusBar::item{border: 0px}')

    def setupThread(self):
        self.workThread = WorkThread(self)
        self.workThread.finished.connect(self.updateMessage)

        self.callThread = CallThread(self)

        self.checkUpgradeThread = CheckUpgradeThread(self)
        self.checkUpgradeThread.doneSignal.connect(self.checkUpgrade)

    def setupSound(self):
        self.ringSound = Sound('ring.wav', conf.value('Monitor/RemindTAFVolume'))
        self.notificationSound = Sound('notification.wav', 100)
        self.alarmSound = Sound('alarm.wav', conf.value('Monitor/WarnTAFVolume'))
        self.trendSound = Sound('trend.wav', conf.value('Monitor/RemindTrendVolume'))
        self.sigmetSound = Sound('sigmet.wav', conf.value('Monitor/RemindSIGMETVolume'))

        self.settingDialog.warnTAFVolume.valueChanged.connect(lambda vol: self.alarmSound.play(volume=vol, loop=False))
        self.settingDialog.remindTAFVolume.valueChanged.connect(lambda vol: self.ringSound.play(volume=vol, loop=False))
        self.settingDialog.remindTrendVolume.valueChanged.connect(lambda vol: self.trendSound.play(volume=vol, loop=False))
        self.settingDialog.remindSIGMETVolume.valueChanged.connect(lambda vol: self.sigmetSound.play(volume=vol, loop=False))

    def changeContract(self):
        target = self.contractsActionGroup.checkedAction()

        if self.contractNo == target:
            conf.setValue('Monitor/SelectedMobile', '')
            logger.info('关闭电话提醒')
        else:
            name = target.text()
            person = db.query(User).filter_by(name=name).first()
            mobile = person.mobile if person else ''

            conf.setValue('Monitor/SelectedMobile', mobile)
            logger.info('切换联系人 %s %s' % (name, mobile))

    def copySelectItem(self, item):
        self.clip.setText(item.text())
        self.statusBar.showMessage(item.text(), 5000)

    def event(self, event):
        """
        捕获事件
        """
        if event.type() == QtCore.QEvent.WindowStateChange and self.isMinimized():
            # 此时窗口已经最小化,
            # 从任务栏中移除窗口
            self.setWindowFlags(self.windowFlags() & QtCore.Qt.Tool)
            self.tray.show()
            return True
        else:
            return super(self.__class__, self).event(event)

    def keyPressEvent(self, event):
        if event.modifiers() == (QtCore.Qt.ShiftModifier | QtCore.Qt.ControlModifier):
            if event.key() == QtCore.Qt.Key_P:
                self.taskTAFEditor.show()
            if event.key() == QtCore.Qt.Key_T:
                self.task_table_dialog.show()

    def closeEvent(self, event):
        if event.spontaneous():
            event.ignore()
            self.hide()
        else:
            self.tafSender.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.trendSender.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.taskTAFSender.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.tafEditor.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.trendEditor.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.taskTAFEditor.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.taskBrowser.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.settingDialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)

            self.tafSender.close()
            self.trendSender.close()
            self.taskTAFSender.close()
            self.tafEditor.close()
            self.trendEditor.close()
            self.taskTAFEditor.close()
            self.taskBrowser.close()
            self.settingDialog.close()

            self.tray.hide()
            event.accept()

    def restoreWindow(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.showNormal()

    def showWindow(self):
        if self.isMinimized():
            self.showNormal()

    def singer(self):
        warnSwitch = self.warnTAFAction.isChecked()
        trendSwitch = boolean(conf.value('Monitor/RemindTrend'))
        sigmetSwitch = boolean(conf.value('Monitor/RemindSIGMET'))

        # 管理趋势声音
        utc = datetime.datetime.utcnow()
        if trendSwitch and utc.minute in (58, 59):
            self.trendSound.play()
        else:
            self.trendSound.stop()

        # 管理报文告警声音
        if warnSwitch and self.context.isWarning():
            self.alarmSound.play()
        else:
            self.alarmSound.stop()

    def reminder(self, tt):
        remindSwitch = boolean(conf.value('Monitor/RemindTAF'))
        if not remindSwitch:
            return None

        clock = self.context.reminder.get(tt)
        current = self.context.current.get(tt)
        warning = self.context.warning.get(tt)

        if clock and not warning and not current['status']:
            text = tt + current['period'][2:]
            self.ringSound.play()
            ret = createAlarmMsgBox(self, text)
            if ret:
                QtCore.QTimer.singleShot(1000 * 60 * 3, lambda: self.reminder(tt))

            self.ringSound.stop()

    def worker(self):
        self.workThread.start()

    def dialer(self, test=False):
        callSwitch = conf.value('Monitor/SelectedMobile')

        if callSwitch and self.context.isWarning() or test:
            self.callThread.start()

    def updateMessage(self):
        listen = Listen(self.context)
        [listen(i) for i in ('FC', 'FT', 'SA', 'SP')]

        self.updateGUI()

    def updateGUI(self):
        self.updateTAFTable()
        self.updateMetarTable()
        self.updateRecent()
        self.updateContractMenu()

        logger.debug('Update GUI')

    def updateContractMenu(self):
        mobile = conf.value('Monitor/SelectedMobile')
        person = db.query(User).filter_by(mobile=mobile).first()
        if person:
            action = getattr(self, 'contract' + str(person.id), None)
            if action:
                action.setChecked(True)
        else:
            self.contractNo.setChecked(True)

    def updateRecent(self):
        self.currentTAF.updateGUI()
        self.recentFT.updateGUI()
        self.recentFC.updateGUI()

    def updateTAFTable(self):
        recent = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
        items = db.query(Tafor).filter(Tafor.sent > recent).order_by(Tafor.sent.desc()).all()
        header = self.tafTable.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tafTable.setRowCount(len(items))
        self.tafTable.setColumnWidth(0, 50)
        self.tafTable.setColumnWidth(2, 140)
        self.tafTable.setColumnWidth(3, 50)
        self.tafTable.setColumnWidth(4, 50)

        for row, item in enumerate(items):
            self.tafTable.setItem(row, 0,  QtWidgets.QTableWidgetItem(item.tt))
            self.tafTable.setItem(row, 1,  QtWidgets.QTableWidgetItem(item.rptInline))
            if item.sent:
                sent = item.sent.strftime("%Y-%m-%d %H:%M:%S")
                self.tafTable.setItem(row, 2,  QtWidgets.QTableWidgetItem(sent))

            if item.confirmed:
                checkedItem = QtWidgets.QTableWidgetItem()
                checkedItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                checkedItem.setIcon(QtGui.QIcon(':/checkmark.png'))
                self.tafTable.setItem(row, 3, checkedItem)
            else:
                checkedItem = QtWidgets.QTableWidgetItem()
                checkedItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                checkedItem.setIcon(QtGui.QIcon(':/cross.png'))
                self.tafTable.setItem(row, 3, checkedItem)

            # if item.task:
            #     task_item = QtWidgets.QTableWidgetItem('√')
            #     # schedule_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            #     # schedule_item.setIcon(QIcon(':/time.png'))
            #     self.tafTable.setItem(row, 4, task_item)


        self.tafTable.setStyleSheet('QTableWidget::item {padding: 5px 0;}')
        self.tafTable.resizeRowsToContents()

    def updateMetarTable(self):
        recent = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
        items = db.query(Metar).filter(Metar.created > recent).order_by(Metar.created.desc()).all()
        header = self.metarTable.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.metarTable.setRowCount(len(items))
        self.metarTable.setColumnWidth(0, 50)

        for row, item in enumerate(items):
            self.metarTable.setItem(row, 0,  QtWidgets.QTableWidgetItem(item.tt))
            self.metarTable.setItem(row, 1,  QtWidgets.QTableWidgetItem(item.rpt))
            if item.tt == 'SP':
                self.metarTable.item(row, 0).setForeground(QtCore.Qt.red)
                self.metarTable.item(row, 1).setForeground(QtCore.Qt.red)

        self.metarTable.setStyleSheet("QTableWidget::item {padding: 5px 0;}")
        self.metarTable.resizeRowsToContents()

    def about(self):
        title = QCoreApplication.translate('MainWindow', 'Terminal Aerodrome Forecast Encoding Software')
        head = '<b>{}</b> v <a href="https://github.com/up1and/tafor">{}</a>'.format(title, __version__)
        description = QCoreApplication.translate('MainWindow', 
                    '''The software is used to encode and post terminal aerodrome forecast, trend forecast, 
                    significant meteorological information, monitor the message, return the alarm by sound or telephone''')
        tail = QCoreApplication.translate('MainWindow', 
                    '''The project is under GPL-2.0 License, Pull Request and Issue are welcome''')
        text = '<p>'.join([head, description, tail, ''])

        QtWidgets.QMessageBox.about(self, title, text)

    def reportIssue(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://github.com/up1and/tafor/issues'))

    def checkUpgrade(self, data):
        hasNewVersion = checkVersion(data.get('tag_name', __version__), __version__)
        if not hasNewVersion:
            return False

        download = 'https://github.com/up1and/tafor/releases'
        title = QCoreApplication.translate('MainWindow', 'Check for Updates')
        text = QCoreApplication.translate('MainWindow', 'New version found {}, do you want to download now?').format(data.get('tag_name'))
        ret = QtWidgets.QMessageBox.question(self, title, text)
        if ret == QtWidgets.QMessageBox.Yes:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl(download))


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    locale = QtCore.QLocale.system().name()
    translateFile = os.path.join(BASEDIR, 'i18n\\translations', '{}.qm'.format(locale))
    if translator.load(translateFile):
        app.installTranslator(translator)

    # QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))

    serverName = 'Tafor'
    socket = QLocalSocket()
    socket.connectToServer(serverName)

    # 如果连接成功，表明server已经存在，当前已有实例在运行
    if socket.waitForConnected(500):
        return(app.quit())

    # 没有实例运行，创建服务器     
    localServer = QLocalServer()
    localServer.listen(serverName)

    try:          
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        logger.error(e, exc_info=True)
    finally:  
        localServer.close()


if __name__ == "__main__":
    main()