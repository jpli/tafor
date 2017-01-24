# -*- coding: utf-8 -*-
import json
import datetime

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from widgets import TAFWidgetsPrimary, TAFWidgetsBecmg, TAFWidgetsTempo
from utils import AFTNMessage, TAFPeriod, Parser, REGEX_TAF
from models import Tafor, Schedule
from config import db


class TAFEditBase(QDialog):
    """docstring for TAF"""

    signal_preview = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(TAFEditBase, self).__init__(parent)
        self.init_ui()
        self.bind_signal()

    def init_ui(self):
        window = QWidget(self)
        layout = QVBoxLayout(window)
        layout.setSizeConstraint(QLayout.SetFixedSize)
        self.primary = TAFWidgetsPrimary()
        self.becmg1, self.becmg2, self.becmg3 = TAFWidgetsBecmg('BECMG1'), TAFWidgetsBecmg('BECMG2'), TAFWidgetsBecmg('BECMG3')
        self.tempo1, self.tempo2 = TAFWidgetsTempo('TEMPO1'), TAFWidgetsTempo('TEMPO2')
        self.next_button = QPushButton()
        self.next_button.setText("下一步")
        layout.addWidget(self.primary)
        layout.addWidget(self.becmg1)
        layout.addWidget(self.becmg2)
        layout.addWidget(self.becmg3)
        layout.addWidget(self.tempo1)
        layout.addWidget(self.tempo2)
        layout.addWidget(self.next_button, 0, Qt.AlignRight|Qt.AlignBottom)
        self.setLayout(layout)

        self.setStyleSheet("QLineEdit {width: 50px;} QComboBox {width: 50px}")

        self.becmg1.hide()
        self.becmg2.hide()
        self.becmg3.hide()
        self.tempo1.hide()
        self.tempo2.hide()

    def bind_signal(self):

        self.primary.becmg1_checkbox.clicked.connect(self.add_becmg_and_tempo)
        self.primary.becmg2_checkbox.clicked.connect(self.add_becmg_and_tempo)
        self.primary.becmg3_checkbox.clicked.connect(self.add_becmg_and_tempo)
        self.primary.tempo1_checkbox.clicked.connect(self.add_becmg_and_tempo)
        self.primary.tempo2_checkbox.clicked.connect(self.add_becmg_and_tempo)

        self.primary.fc.clicked.connect(self.update_message_type)
        self.primary.ft.clicked.connect(self.update_message_type)

        self.primary.normal.clicked.connect(self.update_message_type)
        self.primary.cor.clicked.connect(self.update_message_type)
        self.primary.amd.clicked.connect(self.update_message_type)
        self.primary.cnl.clicked.connect(self.update_message_type)

        self.next_button.clicked.connect(self.assemble_message)
        self.next_button.clicked.connect(self.preview_message)

    def add_becmg_and_tempo(self):
        # BECMG
        if self.primary.becmg1_checkbox.isChecked():
            self.becmg1.setVisible(True)
        else:
            self.becmg1.setVisible(False)
            self.becmg2.setVisible(False)
            self.becmg3.setVisible(False)
            self.primary.becmg2_checkbox.setChecked(False)
            self.primary.becmg3_checkbox.setChecked(False)

        if self.primary.becmg2_checkbox.isChecked():
            self.becmg2.setVisible(True)
        else:
            self.becmg2.setVisible(False)
            self.becmg3.setVisible(False)
            self.primary.becmg3_checkbox.setChecked(False)

        if self.primary.becmg3_checkbox.isChecked():
            self.becmg3.setVisible(True)
        else:
            self.becmg3.setVisible(False)

        # TEMPO
        if self.primary.tempo1_checkbox.isChecked():
            self.tempo1.setVisible(True)
        else:
            self.tempo1.setVisible(False)
            self.tempo2.setVisible(False)
            self.primary.tempo2_checkbox.setChecked(False)

        if self.primary.tempo2_checkbox.isChecked():
            self.tempo2.setVisible(True)
        else:
            self.tempo2.setVisible(False)

    def update_message_type(self):
        if self.primary.fc.isChecked():
            self.tt = 'FC'

        if self.primary.ft.isChecked():
            self.tt = 'FT'

        if self.primary.date.text():
            if self.primary.normal.isChecked():
                self._set_current_period()

                self.primary.ccc.clear()
                self.primary.ccc.setEnabled(False)
                self.primary.aaa.clear()
                self.primary.aaa.setEnabled(False)
                self.primary.aaa_cnl.clear()
                self.primary.aaa_cnl.setEnabled(False)
            else:
                self._set_amd_period()

                if self.primary.cor.isChecked():
                    self.primary.ccc.setEnabled(True)
                    order = self._calc_revision_number('COR')
                    self.primary.ccc.setText(order)
                else:
                    self.primary.ccc.clear()
                    self.primary.ccc.setEnabled(False)

                if self.primary.amd.isChecked():
                    self.primary.aaa.setEnabled(True)
                    order = self._calc_revision_number('AMD')
                    self.primary.aaa.setText(order)
                else:
                    self.primary.aaa.clear()
                    self.primary.aaa.setEnabled(False)

                if self.primary.cnl.isChecked():
                    self.primary.aaa_cnl.setEnabled(True)
                    order = self._calc_revision_number('AMD')
                    self.primary.aaa_cnl.setText(order)
                else:
                    self.primary.aaa_cnl.clear()
                    self.primary.aaa_cnl.setEnabled(False)


    def _set_current_period(self):
        period = TAFPeriod(self.tt, self.time)
        self.current_period = period.current()

        if period.is_existed():
            self.primary.period.setText('')
        else:
            self.primary.period.setText(self.current_period)

    def _set_amd_period(self):
        self.amd_period = TAFPeriod(self.tt, self.time).warn()
        self.primary.period.setText(self.amd_period)

    def _calc_revision_number(self, sign):
        time_limit = datetime.datetime.utcnow() - datetime.timedelta(hours=24)
        query = db.query(Tafor).filter(Tafor.rpt.contains(self.amd_period), Tafor.send_time > time_limit)
        if sign == 'COR':
            items = query.filter(Tafor.rpt.contains('COR')).all()
            print(items)
            order = chr(ord('A') + len(items))
            return 'CC' + order
        elif sign == 'AMD':
            items = query.filter(Tafor.rpt.contains('AMD')).all()
            print(items)
            order = chr(ord('A') + len(items))
            return 'AA' + order


    def assemble_message(self):
        primary_msg = self.primary.message()
        becmg1_msg = self.becmg1.message() if self.primary.becmg1_checkbox.isChecked() else ''
        becmg2_msg = self.becmg2.message() if self.primary.becmg2_checkbox.isChecked() else ''
        becmg3_msg = self.becmg3.message() if self.primary.becmg3_checkbox.isChecked() else ''
        tempo1_msg = self.tempo1.message() if self.primary.tempo1_checkbox.isChecked() else ''
        tempo2_msg = self.tempo2.message() if self.primary.tempo2_checkbox.isChecked() else ''
        msg_list = [primary_msg, becmg1_msg, becmg2_msg, becmg3_msg, tempo1_msg, tempo2_msg]
        self.rpt = '\n'.join(filter(None, msg_list)) + '='
        self.head = self.primary.head()

    def update_date(self):
        self.time = datetime.datetime.utcnow()
        self.primary.date.setText(self.time.strftime('%d%H%M'))


class TAFEdit(TAFEditBase):

    def __init__(self, parent=None):
        super(TAFEdit, self).__init__(parent)

        self.setWindowTitle("编发报文")
        self.setWindowIcon(QIcon(':/fine.png'))

        self.primary.date.setEnabled(False)
        self.update_message_type()

    def preview_message(self):
        message = {'rpt': self.rpt, 'head': self.head}
        self.signal_preview.emit(message)
        print('Emit', message)


class ScheduleTAFEdit(TAFEditBase):

    def __init__(self, parent=None):
        super(ScheduleTAFEdit, self).__init__(parent)

        self.setWindowTitle("定时任务")
        self.setWindowIcon(QIcon(':/schedule.png'))

        self.update_message_type()

        self.primary.group_cls.hide()

        self.primary.date.editingFinished.connect(self.schedule_time)
        self.primary.date.editingFinished.connect(self._set_amd_period)
        self.primary.date.editingFinished.connect(self.change_window_title)
        
    def preview_message(self):
        message = {'head': self.head, 'rpt':self.rpt, 'sch_time': self.time}
        self.signal_preview.emit(message)
        print('Emit', message)

    def schedule_time(self):
        date = self.primary.date.text()
        now = datetime.datetime.utcnow()

        day = int(date[0:2])
        hour = int(date[2:4])
        minute = int(date[4:])

        def _sch_time(time):
            year = time.year
            month = time.month
            return datetime.datetime(year, month, day, hour, minute)

        tmp_time = now
        while _sch_time(tmp_time) < now:
            tmp_time = tmp_time + datetime.timedelta(days=1)

        sch_time = _sch_time(tmp_time)
        self.time = sch_time
        return sch_time

    def change_window_title(self):
        self.setWindowTitle("定时任务   " + self.time.strftime('%Y-%m-%d %H:%M'))



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = TAFEdit()
    ui.show()
    sys.exit(app.exec_())
    
