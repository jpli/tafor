# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Work\tafor\tafor\components\ui\taf_becmg.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(1024, 80)
        Editor.setWindowTitle("BECMG")
        self.verticalLayout = QtWidgets.QVBoxLayout(Editor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout = QtWidgets.QGridLayout()
        self.layout.setObjectName("layout")
        self.intervalLabel = QtWidgets.QLabel(Editor)
        self.intervalLabel.setObjectName("intervalLabel")
        self.layout.addWidget(self.intervalLabel, 2, 4, 1, 1)
        self.cloud2Label = QtWidgets.QLabel(Editor)
        self.cloud2Label.setObjectName("cloud2Label")
        self.layout.addWidget(self.cloud2Label, 2, 12, 1, 1)
        self.cb = QtWidgets.QLineEdit(Editor)
        self.cb.setObjectName("cb")
        self.layout.addWidget(self.cb, 5, 14, 1, 1)
        self.windLabel = QtWidgets.QLabel(Editor)
        self.windLabel.setObjectName("windLabel")
        self.layout.addWidget(self.windLabel, 2, 5, 1, 1)
        self.gustLabel = QtWidgets.QLabel(Editor)
        self.gustLabel.setObjectName("gustLabel")
        self.layout.addWidget(self.gustLabel, 2, 6, 1, 1)
        self.interval = QtWidgets.QLineEdit(Editor)
        self.interval.setObjectName("interval")
        self.layout.addWidget(self.interval, 5, 4, 1, 1)
        self.visLabel = QtWidgets.QLabel(Editor)
        self.visLabel.setObjectName("visLabel")
        self.layout.addWidget(self.visLabel, 2, 7, 1, 1)
        self.cloud3Label = QtWidgets.QLabel(Editor)
        self.cloud3Label.setObjectName("cloud3Label")
        self.layout.addWidget(self.cloud3Label, 2, 13, 1, 1)
        self.vis = QtWidgets.QLineEdit(Editor)
        self.vis.setObjectName("vis")
        self.layout.addWidget(self.vis, 5, 7, 1, 1)
        self.cavok = QtWidgets.QCheckBox(Editor)
        self.cavok.setText("CAVOK")
        self.cavok.setObjectName("cavok")
        self.layout.addWidget(self.cavok, 6, 7, 1, 1)
        self.cloud1 = QtWidgets.QLineEdit(Editor)
        self.cloud1.setObjectName("cloud1")
        self.layout.addWidget(self.cloud1, 5, 11, 1, 1)
        self.cloud3 = QtWidgets.QLineEdit(Editor)
        self.cloud3.setObjectName("cloud3")
        self.layout.addWidget(self.cloud3, 5, 13, 1, 1)
        self.gust = QtWidgets.QLineEdit(Editor)
        self.gust.setObjectName("gust")
        self.layout.addWidget(self.gust, 5, 6, 1, 1)
        self.wind = QtWidgets.QLineEdit(Editor)
        self.wind.setObjectName("wind")
        self.layout.addWidget(self.wind, 5, 5, 1, 1)
        self.cloud2 = QtWidgets.QLineEdit(Editor)
        self.cloud2.setObjectName("cloud2")
        self.layout.addWidget(self.cloud2, 5, 12, 1, 1)
        self.name = QtWidgets.QLabel(Editor)
        self.name.setMinimumSize(QtCore.QSize(76, 0))
        self.name.setStyleSheet("color: rgb(120, 120, 120);")
        self.name.setText("BECMG")
        self.name.setObjectName("name")
        self.layout.addWidget(self.name, 5, 0, 1, 1)
        self.cloud1Label = QtWidgets.QLabel(Editor)
        self.cloud1Label.setObjectName("cloud1Label")
        self.layout.addWidget(self.cloud1Label, 2, 11, 1, 1)
        self.cbLabel = QtWidgets.QLabel(Editor)
        self.cbLabel.setObjectName("cbLabel")
        self.layout.addWidget(self.cbLabel, 2, 14, 1, 1)
        self.weather = QtWidgets.QComboBox(Editor)
        self.weather.setObjectName("weather")
        self.layout.addWidget(self.weather, 5, 10, 1, 1)
        self.weatherWithIntensity = QtWidgets.QComboBox(Editor)
        self.weatherWithIntensity.setObjectName("weatherWithIntensity")
        self.layout.addWidget(self.weatherWithIntensity, 5, 8, 1, 1)
        self.weatherLabel = QtWidgets.QLabel(Editor)
        self.weatherLabel.setObjectName("weatherLabel")
        self.layout.addWidget(self.weatherLabel, 2, 10, 1, 1)
        self.weatherWithIntensityLabel = QtWidgets.QLabel(Editor)
        self.weatherWithIntensityLabel.setObjectName("weatherWithIntensityLabel")
        self.layout.addWidget(self.weatherWithIntensityLabel, 2, 8, 1, 1)
        self.nsc = QtWidgets.QCheckBox(Editor)
        self.nsc.setText("NSC")
        self.nsc.setObjectName("nsc")
        self.layout.addWidget(self.nsc, 6, 11, 1, 1)
        self.verticalLayout.addLayout(self.layout)
        self.intervalLabel.setBuddy(self.interval)
        self.cloud2Label.setBuddy(self.cloud2)
        self.windLabel.setBuddy(self.wind)
        self.gustLabel.setBuddy(self.gust)
        self.visLabel.setBuddy(self.vis)
        self.cloud3Label.setBuddy(self.cloud3)
        self.cloud1Label.setBuddy(self.cloud1)
        self.cbLabel.setBuddy(self.cb)
        self.weatherLabel.setBuddy(self.weather)
        self.weatherWithIntensityLabel.setBuddy(self.weatherWithIntensity)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)
        Editor.setTabOrder(self.interval, self.wind)
        Editor.setTabOrder(self.wind, self.gust)
        Editor.setTabOrder(self.gust, self.vis)
        Editor.setTabOrder(self.vis, self.weatherWithIntensity)
        Editor.setTabOrder(self.weatherWithIntensity, self.weather)
        Editor.setTabOrder(self.weather, self.cloud1)
        Editor.setTabOrder(self.cloud1, self.cloud2)
        Editor.setTabOrder(self.cloud2, self.cloud3)
        Editor.setTabOrder(self.cloud3, self.cb)
        Editor.setTabOrder(self.cb, self.cavok)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        self.intervalLabel.setText(_translate("Editor", "Interval"))
        self.cloud2Label.setText(_translate("Editor", "Cloud2"))
        self.windLabel.setText(_translate("Editor", "Wind"))
        self.gustLabel.setText(_translate("Editor", "Gust"))
        self.visLabel.setText(_translate("Editor", "Visibility"))
        self.cloud3Label.setText(_translate("Editor", "Cloud3"))
        self.cloud1Label.setText(_translate("Editor", "Cloud1"))
        self.cbLabel.setText(_translate("Editor", "Cumulonimbus"))
        self.weatherLabel.setText(_translate("Editor", "Weather2"))
        self.weatherWithIntensityLabel.setText(_translate("Editor", "Weather1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QWidget()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())

