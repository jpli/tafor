import json
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_settings, main_rc
from models import User, Session
from config import db, setting


def to_bool(value):
    # QSetting 读取的值是字符串类型的 false
    # 转换字符串 false 为布尔值 False   字符串 true 为布尔值 True
    return value if isinstance(value, bool) else value.lower() in ('true')


class SettingDialog(QtWidgets.QDialog, Ui_settings.Ui_Settings):
    """docstring for SettingDialog"""
    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/setting.png'))

        # 开机自动启动设置
        self.auto_run_setting = QtCore.QSettings('HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run', QtCore.QSettings.NativeFormat)

        self.bind_signal()
        self.update_contract()
        self.load()

    def bind_signal(self):
        self.add_weather1_button.clicked.connect(lambda: self.add_weather('weather1'))
        self.add_weather2_button.clicked.connect(lambda: self.add_weather('weather2'))

        self.del_weather1_button.clicked.connect(lambda: self.del_weather('weather1'))
        self.del_weather2_button.clicked.connect(lambda: self.del_weather('weather2'))

        self.add_person_button.clicked.connect(self.add_person)
        self.del_person_button.clicked.connect(self.del_person)

        self.button_box.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(self.load)
        self.button_box.button(QtWidgets.QDialogButtonBox.Apply).clicked.connect(self.save)
        self.button_box.accepted.connect(self.save)

    def reset(self):
        print('a')

    def add_weather(self, weather):
        line = getattr(self, weather)
        if line.text():
            getattr(self, weather+'_list').addItem(line.text())
            line.clear()

    def del_weather(self, weather):
        target = getattr(self, weather+'_list')
        target.takeItem(target.currentRow())

    def add_person(self):
        name = self.person_name.text()
        number = self.person_phone_number.text()
        if name and number:
            person = User(name, number)
            db.add(person)
            db.commit()

        self.update_contract()

    def del_person(self):
        row = self.contract_table.currentRow()
        name = self.contract_table.item(row, 0).text()

        person = db.query(User).filter_by(name=name).first()
        db.delete(person)
        db.commit()

        self.update_contract()

    def update_contract(self):
        items = db.query(User).all()
        self.contract_table.setRowCount(len(items))

        for row, item in enumerate(items):
            self.contract_table.setItem(row, 0,  QtWidgets.QTableWidgetItem(item.name))
            self.contract_table.setItem(row, 1,  QtWidgets.QTableWidgetItem(item.phone_number))

        current_contract = self.select_contract.currentText()
        self.select_contract.clear()
        combox_items = [item.name for item in items]
        self.select_contract.addItems(combox_items)
        current_index = self.select_contract.findText(current_contract, QtCore.Qt.MatchFixedString)
        self.select_contract.setCurrentIndex(current_index)


    def save(self):
        import sys

        if self.run_on_start.isChecked():
            self.auto_run_setting.setValue("Tafor.exe", sys.argv[0])
        else:
            self.auto_run_setting.remove("Tafor.exe")

        self.set_value('convention/close_to_minimize', 'close_to_minimize', 'bool')

        self.set_value('message/icao', 'icao')
        self.set_value('message/intelligence', 'intelligence')
        self.set_value('message/fir', 'fir')
        self.set_value('message/trend_sign', 'trend_sign')
        self.set_value('message/weather1', 'weather1_list', 'list')
        self.set_value('message/weather2', 'weather2_list', 'list')

        self.set_value('communication/serial/port', 'port')
        self.set_value('communication/serial/baudrate', 'baudrate')
        self.set_value('communication/serial/parity', 'parity', 'combox')
        self.set_value('communication/serial/bytesize', 'bytesize', 'combox')
        self.set_value('communication/serial/stopbits', 'stopbits', 'combox')

        self.set_value('communication/other/channel', 'channel')
        self.set_value('communication/other/number', 'number')
        self.set_value('communication/other/request_addr', 'request_addr')
        self.set_value('communication/other/user_addr', 'user_addr')

        self.set_value('communication/address/taf', 'taf', 'plaintext')
        self.set_value('communication/address/sigmet', 'sigmet', 'plaintext')
        self.set_value('communication/address/airmet', 'airmet', 'plaintext')
        self.set_value('communication/address/trend', 'trend', 'plaintext')

        self.set_value('monitor/db/sydb', 'sydb', 'bool')
        self.set_value('monitor/db/web', 'web', 'bool')
        self.set_value('monitor/db/sydb_url', 'sydb_url')
        self.set_value('monitor/db/web_url', 'web_url')

        self.set_value('monitor/clock/clock', 'clock', 'bool')
        self.set_value('monitor/clock/clock_time', 'clock_time')
        self.set_value('monitor/clock/clock_volume', 'clock_volume', 'slider')

        self.set_value('monitor/sound/warn_taf', 'warn_taf', 'bool')
        self.set_value('monitor/sound/warn_trend', 'warn_trend', 'bool')
        self.set_value('monitor/sound/warn_sigmet', 'warn_sigmet', 'bool')
        self.set_value('monitor/sound/warn_taf_volume', 'warn_taf_volume', 'slider')
        self.set_value('monitor/sound/warn_trend_volume', 'warn_trend_volume', 'slider')
        self.set_value('monitor/sound/warn_sigmet_volume', 'warn_sigmet_volume', 'slider')

        self.set_value('monitor/phone/phone_warn_taf', 'phone_warn_taf', 'bool')
        self.set_value('monitor/phone/warn_taf_time', 'warn_taf_time')
        self.set_value('monitor/phone/call_service_auth', 'call_service_auth')
        self.set_value('monitor/phone/call_service_url', 'call_service_url')

        self.set_value('monitor/phone/select_phone_number', 'select_contract', 'phone_number')

    def load(self):
        self.run_on_start.setChecked(self.auto_run_setting.contains("Tafor.exe"))

        self.load_value('convention/close_to_minimize', 'close_to_minimize', 'bool')

        self.load_value('message/icao', 'icao')
        self.load_value('message/intelligence', 'intelligence')
        self.load_value('message/fir', 'fir')
        self.load_value('message/trend_sign', 'trend_sign')
        self.load_value('message/weather1', 'weather1_list', 'list')
        self.load_value('message/weather2', 'weather2_list', 'list')

        self.load_value('communication/serial/port', 'port')
        self.load_value('communication/serial/baudrate', 'baudrate')
        self.load_value('communication/serial/parity', 'parity', 'combox')
        self.load_value('communication/serial/bytesize', 'bytesize', 'combox')
        self.load_value('communication/serial/stopbits', 'stopbits', 'combox')

        self.load_value('communication/other/channel', 'channel')
        self.load_value('communication/other/number', 'number')
        self.load_value('communication/other/request_addr', 'request_addr')
        self.load_value('communication/other/user_addr', 'user_addr')

        self.load_value('communication/address/taf', 'taf')
        self.load_value('communication/address/sigmet', 'sigmet')
        self.load_value('communication/address/airmet', 'airmet')
        self.load_value('communication/address/trend', 'trend')

        self.load_value('monitor/db/sydb', 'sydb', 'bool')
        self.load_value('monitor/db/web', 'web', 'bool')
        self.load_value('monitor/db/sydb_url', 'sydb_url')
        self.load_value('monitor/db/web_url', 'web_url')

        self.load_value('monitor/clock/clock', 'clock', 'bool')
        self.load_value('monitor/clock/clock_time', 'clock_time')
        self.load_value('monitor/clock/clock_volume', 'clock_volume', 'slider')

        self.load_value('monitor/sound/warn_taf', 'warn_taf', 'bool')
        self.load_value('monitor/sound/warn_trend', 'warn_trend', 'bool')
        self.load_value('monitor/sound/warn_sigmet', 'warn_sigmet', 'bool')
        self.load_value('monitor/sound/warn_taf_volume', 'warn_taf_volume', 'slider')
        self.load_value('monitor/sound/warn_trend_volume', 'warn_trend_volume', 'slider')
        self.load_value('monitor/sound/warn_sigmet_volume', 'warn_sigmet_volume', 'slider')
        
        self.load_value('monitor/phone/phone_warn_taf', 'phone_warn_taf', 'bool')
        self.load_value('monitor/phone/warn_taf_time', 'warn_taf_time')
        self.load_value('monitor/phone/call_service_auth', 'call_service_auth')
        self.load_value('monitor/phone/call_service_url', 'call_service_url')

        self.load_value('monitor/phone/select_phone_number', 'select_contract', 'phone_number')

    def load_value(self, path, target, mold='text'):

        val = setting.value(path)
        target = getattr(self, target)

        if val is None:
            return 0

        if mold == 'text':
            target.setText(val)

        if mold == 'bool':
            val = to_bool(val)
            target.setChecked(val)

        if mold == 'combox':
            index = target.findText(val, QtCore.Qt.MatchFixedString)
            target.setCurrentIndex(index)

        if mold == 'slider':
            target.setValue(int(val))

        if mold == 'list':
            try:
                items = json.loads(val)
                target.addItems(items)
            except (ValueError, TypeError):
                pass

        if mold == 'phone_number':
            person = db.query(User).filter_by(phone_number=val).first()
            if person:
                index = target.findText(person.name, QtCore.Qt.MatchFixedString)
                target.setCurrentIndex(index)

    def set_value(self, path, target, mold='text'):
        target = getattr(self, target)

        if mold == 'text':
            val = target.text()

        if mold == 'bool':
            val = target.isChecked()

        if mold == 'combox':
            val = target.currentText()

        if mold == 'slider':
            val = target.value()

        if mold == 'plaintext':
            val = target.toPlainText()

        if mold == 'list':
            items = [item.text() for item in target.findItems("", QtCore.Qt.MatchContains)]
            val = json.dumps(items)

        if mold == 'phone_number':
            name = target.currentText()
            person = db.query(User).filter_by(name=name).first()
            val = person.phone_number if person else ''

        setting.setValue(path, val)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = SettingDialog()
    ui.show()
    sys.exit(app.exec_())
    