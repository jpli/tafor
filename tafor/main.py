# -*- coding: utf-8 -*-
import datetime

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui import Ui_main, main_rc
from taf import TAFEdit, ScheduleTAFEdit, ScheduleTAFSend
from setting import SettingDialog
from models import Tafor, Schedule, Session
from widgets import WidgetsItem
from utils import TAFPeriod

__version__ = "1.0.0"


class MainWindow(QMainWindow, Ui_main.Ui_MainWindow):
    """
    主窗口
    """
    def __init__(self, parent=None):
        """
        初始化主窗口
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # 连接TAF对话框
        self.taf_action.triggered.connect(TAFEdit(self).show)

        # 连接设置对话框的槽
        self.setting_action.triggered.connect(SettingDialog(self).show)
        self.setting_action.setIcon(QIcon(':/setting.png'))

        # 连接关于信息的槽
        self.about_action.triggered.connect(self.about)

        # 设置主窗口文字图标
        self.setWindowTitle(u'预报发报软件')
        self.setWindowIcon(QIcon(':/sunny.png'))

        # 设置系统托盘
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(QIcon(':/sunny.png'))
        self.tray.show()

        # 链接系统托盘的槽
        # self.tray.activated.connect(self.restore_window)

        # 添加模块

        self.widget_fc = WidgetsItem()
        self.recent_layout.addWidget(self.widget_fc)

        self.widget_ft = WidgetsItem()
        self.recent_layout.addWidget(self.widget_ft)

        self.db = Session()

        # 自动发送报文的计时器
        self.auto_send_timer = QTimer()
        self.auto_send_timer.timeout.connect(ScheduleTAFSend(self).auto_send)
        self.auto_send_timer.start(15 * 1000) # 15 秒

        # 时钟计时器
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_utc_time)
        self.clock_timer.start(1 * 1000)

        self.warn_timer = QTimer()
        self.warn_timer.timeout.connect(self.update_current_taf)
        self.warn_timer.start(60 * 1000)

        self.update()


    @pyqtSlot("bool")
    def on_warn_action_triggered(self, checked):
        """
        预报报文告警开启开关
        
        @param checked
        @type bool
        """
        print(checked)

    def keyPressEvent(self, event):
        if event.modifiers() == (Qt.ShiftModifier | Qt.ControlModifier) and event.key() == Qt.Key_P:
            ScheduleTAFEdit(self).show()


    def update(self):
        self.update_taf_table()
        self.update_recent()
        self.update_utc_time()
        self.update_current_taf()


    def update_taf_table(self):
        items = self.db.query(Tafor).order_by(Tafor.send_time.desc()).all()
        if len(items) > 12:
            items = items[0:12]
        header = self.taf_table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.taf_table.setRowCount(len(items))
        self.taf_table.setColumnWidth(0, 50)
        self.taf_table.setColumnWidth(2, 140)
        self.taf_table.setColumnWidth(3, 50)
        self.taf_table.setColumnWidth(4, 50)

        for row, item in enumerate(items):
            self.taf_table.setItem(row, 0,  QTableWidgetItem(item.tt))
            self.taf_table.setItem(row, 1,  QTableWidgetItem(item.rpt))
            if item.send_time:
                send_time = item.send_time.strftime("%Y-%m-%d %H:%M:%S")
                self.taf_table.setItem(row, 2,  QTableWidgetItem(send_time))

            if item.confirm_time:
                check_item = QTableWidgetItem('√')
                # check_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                # check_item.setIcon(QIcon(':/check.png'))
                self.taf_table.setItem(row, 3, check_item)
            else:
                check_item = QTableWidgetItem('×')
                # check_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                # check_item.setIcon(QIcon(':/warn.png'))
                self.taf_table.setItem(row, 3, check_item)

            if item.schedule:
                schedule_item = QTableWidgetItem('√')
                # schedule_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                # schedule_item.setIcon(QIcon(':/clock.png'))
                self.taf_table.setItem(row, 4, schedule_item)


        #self.taf_table.setStyleSheet("QTableWidget::item {padding: 5px 0;}")
        # self.taf_table.resizeRowsToContents()


    def update_metar_table(self):
        raise NotImplemented

    def update_recent(self):
        fc = self.db.query(Tafor).filter_by(tt='FC').order_by(Tafor.send_time.desc()).first()
        ft = self.db.query(Tafor).filter_by(tt='FT').order_by(Tafor.send_time.desc()).first()
        # print(fc)
        if fc:
            self.widget_fc.set_item(fc)
        else:
            self.widget_fc.hide()

        if ft:
            self.widget_ft.set_item(ft)
        else:
            self.widget_ft.hide()

    def update_utc_time(self):
        utc = datetime.datetime.utcnow()
        self.utc_time.setText('世界时  ' + utc.strftime("%Y-%m-%d %H:%M:%S"))

    def update_current_taf(self):
        period_fc = TAFPeriod('FC').warn()
        self.current_fc.setText('FC' + period_fc[2:])

        period_ft = TAFPeriod('FT').warn()
        self.current_ft.setText('FT' + period_ft[2:])


    def about(self):
        QMessageBox.about(self, u"预报报文发布软件",
                u"""<b>预报报文发布软件</b> v %s
                <p>暂无
                <p>本项目遵循 GPL-2.0 协议 
                <p>联系邮箱 <a href="mailto:piratecb@gmail.com">piratecb@gmail.com</a>
                """ % (__version__))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    QCoreApplication.setOrganizationName("Up1and")
    QCoreApplication.setOrganizationDomain("up1and.in")
    QCoreApplication.setApplicationName("Tafor")
    ui.show()
    sys.exit(app.exec_())
    