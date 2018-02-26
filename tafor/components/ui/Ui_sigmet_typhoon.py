# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Chen\Work\tafor\tafor\components\ui\sigmet_typhoon.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(500, 164)
        Editor.setWindowTitle("Sigmet")
        self.verticalLayout = QtWidgets.QVBoxLayout(Editor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.descriptionGroup = QtWidgets.QGroupBox(Editor)
        self.descriptionGroup.setObjectName("descriptionGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.descriptionGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.currentLongitude = QtWidgets.QLineEdit(self.descriptionGroup)
        self.currentLongitude.setObjectName("currentLongitude")
        self.gridLayout.addWidget(self.currentLongitude, 1, 1, 1, 1)
        self.currentLatitudeLabel = QtWidgets.QLabel(self.descriptionGroup)
        self.currentLatitudeLabel.setObjectName("currentLatitudeLabel")
        self.gridLayout.addWidget(self.currentLatitudeLabel, 0, 0, 1, 1)
        self.currentLongitudeLabel = QtWidgets.QLabel(self.descriptionGroup)
        self.currentLongitudeLabel.setObjectName("currentLongitudeLabel")
        self.gridLayout.addWidget(self.currentLongitudeLabel, 0, 1, 1, 1)
        self.currentLatitude = QtWidgets.QLineEdit(self.descriptionGroup)
        self.currentLatitude.setObjectName("currentLatitude")
        self.gridLayout.addWidget(self.currentLatitude, 1, 0, 1, 1)
        self.rangeLabel = QtWidgets.QLabel(self.descriptionGroup)
        self.rangeLabel.setObjectName("rangeLabel")
        self.gridLayout.addWidget(self.rangeLabel, 0, 3, 1, 1)
        self.range = QtWidgets.QLineEdit(self.descriptionGroup)
        self.range.setObjectName("range")
        self.gridLayout.addWidget(self.range, 1, 3, 1, 1)
        self.heightLabel = QtWidgets.QLabel(self.descriptionGroup)
        self.heightLabel.setObjectName("heightLabel")
        self.gridLayout.addWidget(self.heightLabel, 0, 2, 1, 1)
        self.height = QtWidgets.QLineEdit(self.descriptionGroup)
        self.height.setObjectName("height")
        self.gridLayout.addWidget(self.height, 1, 2, 1, 1)
        self.speedLabel = QtWidgets.QLabel(self.descriptionGroup)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout.addWidget(self.speedLabel, 0, 5, 1, 1)
        self.movementLabel = QtWidgets.QLabel(self.descriptionGroup)
        self.movementLabel.setObjectName("movementLabel")
        self.gridLayout.addWidget(self.movementLabel, 0, 4, 1, 1)
        self.speed = QtWidgets.QLineEdit(self.descriptionGroup)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 1, 5, 1, 1)
        self.movement = QtWidgets.QComboBox(self.descriptionGroup)
        self.movement.setObjectName("movement")
        self.movement.addItem("")
        self.movement.setItemText(0, "N")
        self.movement.addItem("")
        self.movement.setItemText(1, "NE")
        self.movement.addItem("")
        self.movement.setItemText(2, "E")
        self.movement.addItem("")
        self.movement.setItemText(3, "SE")
        self.movement.addItem("")
        self.movement.setItemText(4, "S")
        self.movement.addItem("")
        self.movement.setItemText(5, "SW")
        self.movement.addItem("")
        self.movement.setItemText(6, "W")
        self.movement.addItem("")
        self.movement.setItemText(7, "NW")
        self.movement.addItem("")
        self.movement.setItemText(8, "STNR")
        self.gridLayout.addWidget(self.movement, 1, 4, 1, 1)
        self.intensityChangeLabel = QtWidgets.QLabel(self.descriptionGroup)
        self.intensityChangeLabel.setObjectName("intensityChangeLabel")
        self.gridLayout.addWidget(self.intensityChangeLabel, 0, 6, 1, 1)
        self.intensityChange = QtWidgets.QComboBox(self.descriptionGroup)
        self.intensityChange.setObjectName("intensityChange")
        self.intensityChange.addItem("")
        self.intensityChange.setItemText(0, "NC")
        self.intensityChange.addItem("")
        self.intensityChange.setItemText(1, "INTSF")
        self.intensityChange.addItem("")
        self.intensityChange.setItemText(2, "WKN")
        self.gridLayout.addWidget(self.intensityChange, 1, 6, 1, 1)
        self.verticalLayout.addWidget(self.descriptionGroup)
        self.forecastGroup = QtWidgets.QGroupBox(Editor)
        self.forecastGroup.setObjectName("forecastGroup")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.forecastGroup)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 3, 1, 1)
        self.forecastTimeLabel = QtWidgets.QLabel(self.forecastGroup)
        self.forecastTimeLabel.setObjectName("forecastTimeLabel")
        self.gridLayout_2.addWidget(self.forecastTimeLabel, 0, 0, 1, 1)
        self.forecastTime = QtWidgets.QLineEdit(self.forecastGroup)
        self.forecastTime.setObjectName("forecastTime")
        self.gridLayout_2.addWidget(self.forecastTime, 1, 0, 1, 1)
        self.forecastLongitude = QtWidgets.QLineEdit(self.forecastGroup)
        self.forecastLongitude.setObjectName("forecastLongitude")
        self.gridLayout_2.addWidget(self.forecastLongitude, 1, 2, 1, 1)
        self.forecastLongitudeLabel = QtWidgets.QLabel(self.forecastGroup)
        self.forecastLongitudeLabel.setObjectName("forecastLongitudeLabel")
        self.gridLayout_2.addWidget(self.forecastLongitudeLabel, 0, 2, 1, 1)
        self.forecastLatitude = QtWidgets.QLineEdit(self.forecastGroup)
        self.forecastLatitude.setObjectName("forecastLatitude")
        self.gridLayout_2.addWidget(self.forecastLatitude, 1, 1, 1, 1)
        self.forecastLatitudeLabel = QtWidgets.QLabel(self.forecastGroup)
        self.forecastLatitudeLabel.setObjectName("forecastLatitudeLabel")
        self.gridLayout_2.addWidget(self.forecastLatitudeLabel, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.forecastGroup)
        self.currentLatitudeLabel.setBuddy(self.currentLatitude)
        self.currentLongitudeLabel.setBuddy(self.currentLongitude)
        self.rangeLabel.setBuddy(self.range)
        self.heightLabel.setBuddy(self.height)
        self.speedLabel.setBuddy(self.speed)
        self.movementLabel.setBuddy(self.movement)
        self.intensityChangeLabel.setBuddy(self.intensityChange)
        self.forecastTimeLabel.setBuddy(self.forecastTime)
        self.forecastLongitudeLabel.setBuddy(self.forecastLongitude)
        self.forecastLatitudeLabel.setBuddy(self.forecastLatitude)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)
        Editor.setTabOrder(self.currentLatitude, self.currentLongitude)
        Editor.setTabOrder(self.currentLongitude, self.height)
        Editor.setTabOrder(self.height, self.range)
        Editor.setTabOrder(self.range, self.movement)
        Editor.setTabOrder(self.movement, self.speed)
        Editor.setTabOrder(self.speed, self.intensityChange)
        Editor.setTabOrder(self.intensityChange, self.forecastTime)
        Editor.setTabOrder(self.forecastTime, self.forecastLatitude)
        Editor.setTabOrder(self.forecastLatitude, self.forecastLongitude)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        self.descriptionGroup.setTitle(_translate("Editor", "Description"))
        self.currentLatitudeLabel.setText(_translate("Editor", "Latitude"))
        self.currentLongitudeLabel.setText(_translate("Editor", "Longitude"))
        self.rangeLabel.setText(_translate("Editor", "Range"))
        self.heightLabel.setText(_translate("Editor", "Height"))
        self.speedLabel.setText(_translate("Editor", "Speed"))
        self.movementLabel.setText(_translate("Editor", "Movement"))
        self.intensityChangeLabel.setText(_translate("Editor", "Intensity Change"))
        self.forecastGroup.setTitle(_translate("Editor", "Forecast"))
        self.forecastTimeLabel.setText(_translate("Editor", "Forecast Time"))
        self.forecastLongitudeLabel.setText(_translate("Editor", "Forecast Longitude"))
        self.forecastLatitudeLabel.setText(_translate("Editor", "Forecast Latitude"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QWidget()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())
