# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Chen\Work\tafor\tafor\ui\setting.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(563, 433)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main = QtWidgets.QHBoxLayout()
        self.main.setObjectName("main")
        self.left_side = QtWidgets.QWidget(Dialog)
        self.left_side.setMaximumSize(QtCore.QSize(120, 16777215))
        self.left_side.setObjectName("left_side")
        self.leftbox = QtWidgets.QVBoxLayout(self.left_side)
        self.leftbox.setContentsMargins(0, 0, 0, 0)
        self.leftbox.setObjectName("leftbox")
        self.search = QtWidgets.QLineEdit(self.left_side)
        self.search.setObjectName("search")
        self.leftbox.addWidget(self.search)
        self.menu = QtWidgets.QListWidget(self.left_side)
        self.menu.setObjectName("menu")
        item = QtWidgets.QListWidgetItem()
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.menu.addItem(item)
        self.leftbox.addWidget(self.menu)
        self.main.addWidget(self.left_side)
        self.stacked = QtWidgets.QStackedWidget(Dialog)
        self.stacked.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stacked.setObjectName("stacked")
        self.message_page = QtWidgets.QWidget()
        self.message_page.setObjectName("message_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.message_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.prefix_group = QtWidgets.QGroupBox(self.message_page)
        self.prefix_group.setObjectName("prefix_group")
        self.formLayout = QtWidgets.QFormLayout(self.prefix_group)
        self.formLayout.setObjectName("formLayout")
        self.icao_label = QtWidgets.QLabel(self.prefix_group)
        self.icao_label.setObjectName("icao_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.icao_label)
        self.icao = QtWidgets.QLineEdit(self.prefix_group)
        self.icao.setObjectName("icao")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.icao)
        self.intelligence_label = QtWidgets.QLabel(self.prefix_group)
        self.intelligence_label.setObjectName("intelligence_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.intelligence_label)
        self.intelligence = QtWidgets.QLineEdit(self.prefix_group)
        self.intelligence.setObjectName("intelligence")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.intelligence)
        self.fir_label = QtWidgets.QLabel(self.prefix_group)
        self.fir_label.setObjectName("fir_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.fir_label)
        self.fir = QtWidgets.QLineEdit(self.prefix_group)
        self.fir.setObjectName("fir")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fir)
        self.trend_label = QtWidgets.QLabel(self.prefix_group)
        self.trend_label.setObjectName("trend_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.trend_label)
        self.trend = QtWidgets.QLineEdit(self.prefix_group)
        self.trend.setObjectName("trend")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.trend)
        self.verticalLayout_2.addWidget(self.prefix_group)
        self.weather_group = QtWidgets.QGroupBox(self.message_page)
        self.weather_group.setObjectName("weather_group")
        self.gridLayout = QtWidgets.QGridLayout(self.weather_group)
        self.gridLayout.setObjectName("gridLayout")
        self.wx1_edit_layout = QtWidgets.QHBoxLayout()
        self.wx1_edit_layout.setObjectName("wx1_edit_layout")
        self.weather1 = QtWidgets.QLineEdit(self.weather_group)
        self.weather1.setText("")
        self.weather1.setObjectName("weather1")
        self.wx1_edit_layout.addWidget(self.weather1)
        self.weather1_add_button = QtWidgets.QPushButton(self.weather_group)
        self.weather1_add_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.weather1_add_button.setObjectName("weather1_add_button")
        self.wx1_edit_layout.addWidget(self.weather1_add_button)
        self.weather1_del_button = QtWidgets.QPushButton(self.weather_group)
        self.weather1_del_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.weather1_del_button.setObjectName("weather1_del_button")
        self.wx1_edit_layout.addWidget(self.weather1_del_button)
        self.gridLayout.addLayout(self.wx1_edit_layout, 0, 0, 1, 1)
        self.weather2_list = QtWidgets.QListWidget(self.weather_group)
        self.weather2_list.setObjectName("weather2_list")
        item = QtWidgets.QListWidgetItem()
        self.weather2_list.addItem(item)
        self.gridLayout.addWidget(self.weather2_list, 1, 1, 1, 1)
        self.weather1_list = QtWidgets.QListWidget(self.weather_group)
        self.weather1_list.setObjectName("weather1_list")
        item = QtWidgets.QListWidgetItem()
        self.weather1_list.addItem(item)
        self.gridLayout.addWidget(self.weather1_list, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.weather2 = QtWidgets.QLineEdit(self.weather_group)
        self.weather2.setObjectName("weather2")
        self.horizontalLayout_4.addWidget(self.weather2)
        self.weather2_add_button = QtWidgets.QPushButton(self.weather_group)
        self.weather2_add_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.weather2_add_button.setObjectName("weather2_add_button")
        self.horizontalLayout_4.addWidget(self.weather2_add_button)
        self.weather2_del_button = QtWidgets.QPushButton(self.weather_group)
        self.weather2_del_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.weather2_del_button.setObjectName("weather2_del_button")
        self.horizontalLayout_4.addWidget(self.weather2_del_button)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.weather_group)
        self.stacked.addWidget(self.message_page)
        self.communication_page = QtWidgets.QWidget()
        self.communication_page.setObjectName("communication_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.communication_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.setObjectName("top_layout")
        self.serial_group = QtWidgets.QGroupBox(self.communication_page)
        self.serial_group.setObjectName("serial_group")
        self.formLayout_3 = QtWidgets.QFormLayout(self.serial_group)
        self.formLayout_3.setObjectName("formLayout_3")
        self.port_label = QtWidgets.QLabel(self.serial_group)
        self.port_label.setObjectName("port_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.port_label)
        self.port = QtWidgets.QLineEdit(self.serial_group)
        self.port.setObjectName("port")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.port)
        self.baudrate_label = QtWidgets.QLabel(self.serial_group)
        self.baudrate_label.setObjectName("baudrate_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.baudrate_label)
        self.baudrate = QtWidgets.QLineEdit(self.serial_group)
        self.baudrate.setObjectName("baudrate")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.baudrate)
        self.parity_label = QtWidgets.QLabel(self.serial_group)
        self.parity_label.setObjectName("parity_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.parity_label)
        self.parity = QtWidgets.QComboBox(self.serial_group)
        self.parity.setObjectName("parity")
        self.parity.addItem("")
        self.parity.addItem("")
        self.parity.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.parity)
        self.bytesize_label = QtWidgets.QLabel(self.serial_group)
        self.bytesize_label.setObjectName("bytesize_label")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.bytesize_label)
        self.bytesize = QtWidgets.QComboBox(self.serial_group)
        self.bytesize.setObjectName("bytesize")
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bytesize)
        self.stopbits_label = QtWidgets.QLabel(self.serial_group)
        self.stopbits_label.setObjectName("stopbits_label")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.stopbits_label)
        self.stopbits = QtWidgets.QComboBox(self.serial_group)
        self.stopbits.setObjectName("stopbits")
        self.stopbits.addItem("")
        self.stopbits.addItem("")
        self.stopbits.addItem("")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.stopbits)
        self.top_layout.addWidget(self.serial_group)
        self.other_group = QtWidgets.QGroupBox(self.communication_page)
        self.other_group.setObjectName("other_group")
        self.formLayout_7 = QtWidgets.QFormLayout(self.other_group)
        self.formLayout_7.setObjectName("formLayout_7")
        self.line_label = QtWidgets.QLabel(self.other_group)
        self.line_label.setObjectName("line_label")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.line_label)
        self.line = QtWidgets.QLineEdit(self.other_group)
        self.line.setObjectName("line")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line)
        self.number_label = QtWidgets.QLabel(self.other_group)
        self.number_label.setObjectName("number_label")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.number_label)
        self.number = QtWidgets.QLineEdit(self.other_group)
        self.number.setObjectName("number")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.number)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_7.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.request_addr = QtWidgets.QLineEdit(self.other_group)
        self.request_addr.setObjectName("request_addr")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.request_addr)
        self.request_addr_label = QtWidgets.QLabel(self.other_group)
        self.request_addr_label.setObjectName("request_addr_label")
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.request_addr_label)
        self.user_addr = QtWidgets.QLineEdit(self.other_group)
        self.user_addr.setObjectName("user_addr")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.user_addr)
        self.user_addr_label = QtWidgets.QLabel(self.other_group)
        self.user_addr_label.setObjectName("user_addr_label")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.user_addr_label)
        self.top_layout.addWidget(self.other_group)
        self.verticalLayout_4.addLayout(self.top_layout)
        self.send_addr_group = QtWidgets.QGroupBox(self.communication_page)
        self.send_addr_group.setObjectName("send_addr_group")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.send_addr_group)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.send_addr_group)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_taf = QtWidgets.QWidget()
        self.tab_taf.setObjectName("tab_taf")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_taf)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.taf_addr = QtWidgets.QTextEdit(self.tab_taf)
        self.taf_addr.setObjectName("taf_addr")
        self.verticalLayout_3.addWidget(self.taf_addr)
        self.tabWidget.addTab(self.tab_taf, "")
        self.tab_sigmet = QtWidgets.QWidget()
        self.tab_sigmet.setObjectName("tab_sigmet")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_sigmet)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.sigmet_addr = QtWidgets.QTextEdit(self.tab_sigmet)
        self.sigmet_addr.setObjectName("sigmet_addr")
        self.verticalLayout_7.addWidget(self.sigmet_addr)
        self.tabWidget.addTab(self.tab_sigmet, "")
        self.tab_airmet = QtWidgets.QWidget()
        self.tab_airmet.setObjectName("tab_airmet")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_airmet)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.airmet_addr = QtWidgets.QTextEdit(self.tab_airmet)
        self.airmet_addr.setObjectName("airmet_addr")
        self.verticalLayout_8.addWidget(self.airmet_addr)
        self.tabWidget.addTab(self.tab_airmet, "")
        self.tab_trend = QtWidgets.QWidget()
        self.tab_trend.setObjectName("tab_trend")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_trend)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.trend_addr = QtWidgets.QTextEdit(self.tab_trend)
        self.trend_addr.setObjectName("trend_addr")
        self.verticalLayout_9.addWidget(self.trend_addr)
        self.tabWidget.addTab(self.tab_trend, "")
        self.verticalLayout_10.addWidget(self.tabWidget)
        self.verticalLayout_4.addWidget(self.send_addr_group)
        self.stacked.addWidget(self.communication_page)
        self.monitor_page = QtWidgets.QWidget()
        self.monitor_page.setObjectName("monitor_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.monitor_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.db_source_group = QtWidgets.QGroupBox(self.monitor_page)
        self.db_source_group.setObjectName("db_source_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.db_source_group)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sydb = QtWidgets.QRadioButton(self.db_source_group)
        self.sydb.setChecked(True)
        self.sydb.setObjectName("sydb")
        self.gridLayout_2.addWidget(self.sydb, 0, 0, 1, 1)
        self.web = QtWidgets.QRadioButton(self.db_source_group)
        self.web.setObjectName("web")
        self.gridLayout_2.addWidget(self.web, 0, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.db_source_group)
        self.clock_group = QtWidgets.QGroupBox(self.monitor_page)
        self.clock_group.setObjectName("clock_group")
        self.formLayout_5 = QtWidgets.QFormLayout(self.clock_group)
        self.formLayout_5.setObjectName("formLayout_5")
        self.clock = QtWidgets.QCheckBox(self.clock_group)
        self.clock.setObjectName("clock")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.clock)
        self.clock_time_label = QtWidgets.QLabel(self.clock_group)
        self.clock_time_label.setObjectName("clock_time_label")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.clock_time_label)
        self.clock_time = QtWidgets.QLineEdit(self.clock_group)
        self.clock_time.setMaximumSize(QtCore.QSize(120, 16777215))
        self.clock_time.setObjectName("clock_time")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.clock_time)
        self.clock_volume_label = QtWidgets.QLabel(self.clock_group)
        self.clock_volume_label.setObjectName("clock_volume_label")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.clock_volume_label)
        self.clock_volume = QtWidgets.QSlider(self.clock_group)
        self.clock_volume.setOrientation(QtCore.Qt.Horizontal)
        self.clock_volume.setObjectName("clock_volume")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clock_volume)
        self.verticalLayout_5.addWidget(self.clock_group)
        self.sound_group = QtWidgets.QGroupBox(self.monitor_page)
        self.sound_group.setObjectName("sound_group")
        self.formLayout_2 = QtWidgets.QFormLayout(self.sound_group)
        self.formLayout_2.setObjectName("formLayout_2")
        self.warn_taf = QtWidgets.QCheckBox(self.sound_group)
        self.warn_taf.setObjectName("warn_taf")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.warn_taf)
        self.warn_taf_volume = QtWidgets.QSlider(self.sound_group)
        self.warn_taf_volume.setOrientation(QtCore.Qt.Horizontal)
        self.warn_taf_volume.setObjectName("warn_taf_volume")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.warn_taf_volume)
        self.warn_trend = QtWidgets.QCheckBox(self.sound_group)
        self.warn_trend.setObjectName("warn_trend")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.warn_trend)
        self.warn_trend_volume = QtWidgets.QSlider(self.sound_group)
        self.warn_trend_volume.setOrientation(QtCore.Qt.Horizontal)
        self.warn_trend_volume.setObjectName("warn_trend_volume")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.warn_trend_volume)
        self.warn_sigmet = QtWidgets.QCheckBox(self.sound_group)
        self.warn_sigmet.setObjectName("warn_sigmet")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.warn_sigmet)
        self.warn_sigmet_volume = QtWidgets.QSlider(self.sound_group)
        self.warn_sigmet_volume.setOrientation(QtCore.Qt.Horizontal)
        self.warn_sigmet_volume.setObjectName("warn_sigmet_volume")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.warn_sigmet_volume)
        self.verticalLayout_5.addWidget(self.sound_group)
        self.phone_group = QtWidgets.QGroupBox(self.monitor_page)
        self.phone_group.setObjectName("phone_group")
        self.formLayout_4 = QtWidgets.QFormLayout(self.phone_group)
        self.formLayout_4.setObjectName("formLayout_4")
        self.phone_warn_taf = QtWidgets.QCheckBox(self.phone_group)
        self.phone_warn_taf.setObjectName("phone_warn_taf")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.phone_warn_taf)
        self.warn_taf_time_label = QtWidgets.QLabel(self.phone_group)
        self.warn_taf_time_label.setObjectName("warn_taf_time_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.warn_taf_time_label)
        self.warn_taf_time = QtWidgets.QLineEdit(self.phone_group)
        self.warn_taf_time.setMaximumSize(QtCore.QSize(120, 16777215))
        self.warn_taf_time.setObjectName("warn_taf_time")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.warn_taf_time)
        self.phone_number_label = QtWidgets.QLabel(self.phone_group)
        self.phone_number_label.setObjectName("phone_number_label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.phone_number_label)
        self.phone_number = QtWidgets.QComboBox(self.phone_group)
        self.phone_number.setMaximumSize(QtCore.QSize(120, 16777215))
        self.phone_number.setObjectName("phone_number")
        self.phone_number.addItem("")
        self.phone_number.addItem("")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.phone_number)
        self.verticalLayout_5.addWidget(self.phone_group)
        self.stacked.addWidget(self.monitor_page)
        self.convention_page = QtWidgets.QWidget()
        self.convention_page.setObjectName("convention_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.convention_page)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.convention_group = QtWidgets.QGroupBox(self.convention_page)
        self.convention_group.setObjectName("convention_group")
        self.formLayout_8 = QtWidgets.QFormLayout(self.convention_group)
        self.formLayout_8.setObjectName("formLayout_8")
        self.run_on_start = QtWidgets.QCheckBox(self.convention_group)
        self.run_on_start.setObjectName("run_on_start")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.run_on_start)
        self.close_to_minimize = QtWidgets.QCheckBox(self.convention_group)
        self.close_to_minimize.setObjectName("close_to_minimize")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.close_to_minimize)
        self.verticalLayout_6.addWidget(self.convention_group)
        self.backup_group = QtWidgets.QGroupBox(self.convention_page)
        self.backup_group.setObjectName("backup_group")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.backup_group)
        self.gridLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.import_path = QtWidgets.QLineEdit(self.backup_group)
        self.import_path.setObjectName("import_path")
        self.gridLayout_5.addWidget(self.import_path, 0, 0, 1, 1)
        self.export_button = QtWidgets.QPushButton(self.backup_group)
        self.export_button.setObjectName("export_button")
        self.gridLayout_5.addWidget(self.export_button, 1, 2, 1, 1)
        self.import_button = QtWidgets.QPushButton(self.backup_group)
        self.import_button.setObjectName("import_button")
        self.gridLayout_5.addWidget(self.import_button, 0, 2, 1, 1)
        self.import_explore = QtWidgets.QPushButton(self.backup_group)
        self.import_explore.setObjectName("import_explore")
        self.gridLayout_5.addWidget(self.import_explore, 0, 1, 1, 1)
        self.export_explore = QtWidgets.QPushButton(self.backup_group)
        self.export_explore.setObjectName("export_explore")
        self.gridLayout_5.addWidget(self.export_explore, 1, 1, 1, 1)
        self.export_path = QtWidgets.QLineEdit(self.backup_group)
        self.export_path.setObjectName("export_path")
        self.gridLayout_5.addWidget(self.export_path, 1, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.backup_group)
        self.stacked.addWidget(self.convention_page)
        self.main.addWidget(self.stacked)
        self.verticalLayout.addLayout(self.main)
        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(Dialog)
        self.stacked.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(3)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)
        self.menu.currentRowChanged['int'].connect(self.stacked.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.search, self.menu)
        Dialog.setTabOrder(self.menu, self.icao)
        Dialog.setTabOrder(self.icao, self.intelligence)
        Dialog.setTabOrder(self.intelligence, self.fir)
        Dialog.setTabOrder(self.fir, self.trend)
        Dialog.setTabOrder(self.trend, self.weather1)
        Dialog.setTabOrder(self.weather1, self.weather1_add_button)
        Dialog.setTabOrder(self.weather1_add_button, self.weather1_del_button)
        Dialog.setTabOrder(self.weather1_del_button, self.weather1_list)
        Dialog.setTabOrder(self.weather1_list, self.weather2)
        Dialog.setTabOrder(self.weather2, self.weather2_add_button)
        Dialog.setTabOrder(self.weather2_add_button, self.weather2_del_button)
        Dialog.setTabOrder(self.weather2_del_button, self.weather2_list)
        Dialog.setTabOrder(self.weather2_list, self.port)
        Dialog.setTabOrder(self.port, self.baudrate)
        Dialog.setTabOrder(self.baudrate, self.parity)
        Dialog.setTabOrder(self.parity, self.bytesize)
        Dialog.setTabOrder(self.bytesize, self.stopbits)
        Dialog.setTabOrder(self.stopbits, self.line)
        Dialog.setTabOrder(self.line, self.number)
        Dialog.setTabOrder(self.number, self.request_addr)
        Dialog.setTabOrder(self.request_addr, self.user_addr)
        Dialog.setTabOrder(self.user_addr, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.taf_addr)
        Dialog.setTabOrder(self.taf_addr, self.sigmet_addr)
        Dialog.setTabOrder(self.sigmet_addr, self.airmet_addr)
        Dialog.setTabOrder(self.airmet_addr, self.trend_addr)
        Dialog.setTabOrder(self.trend_addr, self.sydb)
        Dialog.setTabOrder(self.sydb, self.web)
        Dialog.setTabOrder(self.web, self.clock)
        Dialog.setTabOrder(self.clock, self.clock_time)
        Dialog.setTabOrder(self.clock_time, self.clock_volume)
        Dialog.setTabOrder(self.clock_volume, self.warn_taf)
        Dialog.setTabOrder(self.warn_taf, self.warn_taf_volume)
        Dialog.setTabOrder(self.warn_taf_volume, self.warn_trend)
        Dialog.setTabOrder(self.warn_trend, self.warn_trend_volume)
        Dialog.setTabOrder(self.warn_trend_volume, self.warn_sigmet)
        Dialog.setTabOrder(self.warn_sigmet, self.warn_sigmet_volume)
        Dialog.setTabOrder(self.warn_sigmet_volume, self.phone_warn_taf)
        Dialog.setTabOrder(self.phone_warn_taf, self.warn_taf_time)
        Dialog.setTabOrder(self.warn_taf_time, self.phone_number)
        Dialog.setTabOrder(self.phone_number, self.run_on_start)
        Dialog.setTabOrder(self.run_on_start, self.close_to_minimize)
        Dialog.setTabOrder(self.close_to_minimize, self.import_path)
        Dialog.setTabOrder(self.import_path, self.import_explore)
        Dialog.setTabOrder(self.import_explore, self.import_button)
        Dialog.setTabOrder(self.import_button, self.export_path)
        Dialog.setTabOrder(self.export_path, self.export_explore)
        Dialog.setTabOrder(self.export_explore, self.export_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置"))
        __sortingEnabled = self.menu.isSortingEnabled()
        self.menu.setSortingEnabled(False)
        item = self.menu.item(0)
        item.setText(_translate("Dialog", "编报"))
        item = self.menu.item(1)
        item.setText(_translate("Dialog", "通信"))
        item = self.menu.item(2)
        item.setText(_translate("Dialog", "监控"))
        item = self.menu.item(3)
        item.setText(_translate("Dialog", "常规"))
        self.menu.setSortingEnabled(__sortingEnabled)
        self.prefix_group.setTitle(_translate("Dialog", "前缀"))
        self.icao_label.setText(_translate("Dialog", "机场代码"))
        self.icao.setPlaceholderText(_translate("Dialog", "ZJHK"))
        self.intelligence_label.setText(_translate("Dialog", "气象情报"))
        self.intelligence.setPlaceholderText(_translate("Dialog", "CI35"))
        self.fir_label.setText(_translate("Dialog", "监视台责任区"))
        self.fir.setPlaceholderText(_translate("Dialog", "ZJSA SANYA FIR"))
        self.trend_label.setText(_translate("Dialog", "趋势识别码"))
        self.trend.setPlaceholderText(_translate("Dialog", "TREND"))
        self.weather_group.setTitle(_translate("Dialog", "天气现象备案"))
        self.weather1.setPlaceholderText(_translate("Dialog", "有强度变化的天气现象"))
        self.weather1_add_button.setText(_translate("Dialog", "+"))
        self.weather1_del_button.setText(_translate("Dialog", "—"))
        __sortingEnabled = self.weather2_list.isSortingEnabled()
        self.weather2_list.setSortingEnabled(False)
        item = self.weather2_list.item(0)
        item.setText(_translate("Dialog", "BR"))
        self.weather2_list.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.weather1_list.isSortingEnabled()
        self.weather1_list.setSortingEnabled(False)
        item = self.weather1_list.item(0)
        item.setText(_translate("Dialog", "+TSRA"))
        self.weather1_list.setSortingEnabled(__sortingEnabled)
        self.weather2.setPlaceholderText(_translate("Dialog", "无强度变化的天气现象"))
        self.weather2_add_button.setText(_translate("Dialog", "+"))
        self.weather2_del_button.setText(_translate("Dialog", "—"))
        self.serial_group.setTitle(_translate("Dialog", "串口参数"))
        self.port_label.setText(_translate("Dialog", "端口"))
        self.port.setPlaceholderText(_translate("Dialog", "COM1"))
        self.baudrate_label.setText(_translate("Dialog", "波特率"))
        self.baudrate.setPlaceholderText(_translate("Dialog", "9600"))
        self.parity_label.setText(_translate("Dialog", "校验位"))
        self.parity.setItemText(0, _translate("Dialog", "NONE"))
        self.parity.setItemText(1, _translate("Dialog", "EVEN"))
        self.parity.setItemText(2, _translate("Dialog", "ODD"))
        self.bytesize_label.setText(_translate("Dialog", "数据位"))
        self.bytesize.setItemText(0, _translate("Dialog", "5"))
        self.bytesize.setItemText(1, _translate("Dialog", "6"))
        self.bytesize.setItemText(2, _translate("Dialog", "7"))
        self.bytesize.setItemText(3, _translate("Dialog", "8"))
        self.stopbits_label.setText(_translate("Dialog", "停止位"))
        self.stopbits.setItemText(0, _translate("Dialog", "1"))
        self.stopbits.setItemText(1, _translate("Dialog", "1.5"))
        self.stopbits.setItemText(2, _translate("Dialog", "2"))
        self.other_group.setTitle(_translate("Dialog", "其他"))
        self.line_label.setText(_translate("Dialog", "线路冠字"))
        self.line.setPlaceholderText(_translate("Dialog", "YMA"))
        self.number_label.setText(_translate("Dialog", "流水号"))
        self.number.setPlaceholderText(_translate("Dialog", "1"))
        self.request_addr.setPlaceholderText(_translate("Dialog", "ZGGGYZYX"))
        self.request_addr_label.setText(_translate("Dialog", "请求地址"))
        self.user_addr.setPlaceholderText(_translate("Dialog", "ZJHKYMYX"))
        self.user_addr_label.setText(_translate("Dialog", "用户单位"))
        self.send_addr_group.setTitle(_translate("Dialog", "发报地址"))
        self.taf_addr.setPlaceholderText(_translate("Dialog", "发报地址请以空格分隔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_taf), _translate("Dialog", "TAF"))
        self.sigmet_addr.setPlaceholderText(_translate("Dialog", "发报地址请以空格分隔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sigmet), _translate("Dialog", "SIGMET"))
        self.airmet_addr.setPlaceholderText(_translate("Dialog", "发报地址请以空格分隔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_airmet), _translate("Dialog", "AIRMET"))
        self.trend_addr.setPlaceholderText(_translate("Dialog", "发报地址请以空格分隔"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_trend), _translate("Dialog", "TREND"))
        self.db_source_group.setTitle(_translate("Dialog", "监控数据源"))
        self.sydb.setText(_translate("Dialog", "三亚区管数据库"))
        self.web.setText(_translate("Dialog", "中南综合信息服务系统"))
        self.clock_group.setTitle(_translate("Dialog", "闹钟和音量"))
        self.clock.setText(_translate("Dialog", "启用    "))
        self.clock_time_label.setText(_translate("Dialog", "闹铃时间        "))
        self.clock_time.setPlaceholderText(_translate("Dialog", "时间单位分钟"))
        self.clock_volume_label.setText(_translate("Dialog", "音量"))
        self.sound_group.setTitle(_translate("Dialog", "声音提醒和音量"))
        self.warn_taf.setText(_translate("Dialog", "报文迟发"))
        self.warn_trend.setText(_translate("Dialog", "趋势预报"))
        self.warn_sigmet.setText(_translate("Dialog", "重要气象情报"))
        self.phone_group.setTitle(_translate("Dialog", "电话"))
        self.phone_warn_taf.setText(_translate("Dialog", "报文迟发"))
        self.warn_taf_time_label.setText(_translate("Dialog", "提醒时间        "))
        self.warn_taf_time.setPlaceholderText(_translate("Dialog", "时间单位分钟"))
        self.phone_number_label.setText(_translate("Dialog", "电话"))
        self.phone_number.setItemText(0, _translate("Dialog", "预报室"))
        self.phone_number.setItemText(1, _translate("Dialog", "陈彬"))
        self.convention_group.setTitle(_translate("Dialog", "常规"))
        self.run_on_start.setText(_translate("Dialog", "开机自动启动"))
        self.close_to_minimize.setText(_translate("Dialog", "关闭时最小化到系统托盘"))
        self.backup_group.setTitle(_translate("Dialog", "备份"))
        self.import_path.setPlaceholderText(_translate("Dialog", "PATH"))
        self.export_button.setText(_translate("Dialog", "导出"))
        self.import_button.setText(_translate("Dialog", "导入"))
        self.import_explore.setText(_translate("Dialog", "浏览"))
        self.export_explore.setText(_translate("Dialog", "浏览"))
        self.export_path.setPlaceholderText(_translate("Dialog", "PATH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

