# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Work\tafor\tafor\components\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(882, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainTab = QtWidgets.QTabWidget(self.centralWidget)
        self.mainTab.setMinimumSize(QtCore.QSize(850, 500))
        self.mainTab.setMovable(True)
        self.mainTab.setObjectName("mainTab")
        self.recentTab = QtWidgets.QWidget()
        self.recentTab.setObjectName("recentTab")
        self.recentLayout = QtWidgets.QVBoxLayout(self.recentTab)
        self.recentLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.recentLayout.setContentsMargins(0, 0, 0, 0)
        self.recentLayout.setObjectName("recentLayout")
        self.tips = QtWidgets.QWidget(self.recentTab)
        self.tips.setMinimumSize(QtCore.QSize(840, 0))
        self.tips.setObjectName("tips")
        self.tipsLayout = QtWidgets.QHBoxLayout(self.tips)
        self.tipsLayout.setContentsMargins(10, 20, 10, 20)
        self.tipsLayout.setObjectName("tipsLayout")
        self.recentLayout.addWidget(self.tips)
        self.mainTab.addTab(self.recentTab, "")
        self.tafTab = QtWidgets.QWidget()
        self.tafTab.setObjectName("tafTab")
        self.taf_layout = QtWidgets.QVBoxLayout(self.tafTab)
        self.taf_layout.setContentsMargins(0, 0, 0, 0)
        self.taf_layout.setObjectName("taf_layout")
        self.tafTable = QtWidgets.QTableWidget(self.tafTab)
        self.tafTable.setMinimumSize(QtCore.QSize(850, 500))
        self.tafTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tafTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tafTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tafTable.setObjectName("tafTable")
        self.tafTable.setColumnCount(5)
        self.tafTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tafTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tafTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tafTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tafTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tafTable.setHorizontalHeaderItem(4, item)
        self.taf_layout.addWidget(self.tafTable)
        self.mainTab.addTab(self.tafTab, "")
        self.metarTab = QtWidgets.QWidget()
        self.metarTab.setObjectName("metarTab")
        self.metar_layout = QtWidgets.QVBoxLayout(self.metarTab)
        self.metar_layout.setContentsMargins(0, 0, 0, 0)
        self.metar_layout.setObjectName("metar_layout")
        self.metarTable = QtWidgets.QTableWidget(self.metarTab)
        self.metarTable.setMinimumSize(QtCore.QSize(850, 500))
        self.metarTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.metarTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.metarTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.metarTable.setObjectName("metarTable")
        self.metarTable.setColumnCount(2)
        self.metarTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.metarTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.metarTable.setHorizontalHeaderItem(1, item)
        self.metar_layout.addWidget(self.metarTable)
        self.mainTab.addTab(self.metarTab, "")
        self.verticalLayout.addWidget(self.mainTab)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 882, 23))
        self.menuBar.setObjectName("menuBar")
        self.postMenu = QtWidgets.QMenu(self.menuBar)
        self.postMenu.setObjectName("postMenu")
        self.settingMenu = QtWidgets.QMenu(self.menuBar)
        self.settingMenu.setObjectName("settingMenu")
        self.contractsMenu = QtWidgets.QMenu(self.settingMenu)
        self.contractsMenu.setObjectName("contractsMenu")
        self.helpMenu = QtWidgets.QMenu(self.menuBar)
        self.helpMenu.setObjectName("helpMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.tafAction = QtWidgets.QAction(MainWindow)
        self.tafAction.setObjectName("tafAction")
        self.trendAction = QtWidgets.QAction(MainWindow)
        self.trendAction.setObjectName("trendAction")
        self.sigmetAction = QtWidgets.QAction(MainWindow)
        self.sigmetAction.setObjectName("sigmetAction")
        self.settingAction = QtWidgets.QAction(MainWindow)
        self.settingAction.setObjectName("settingAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.quitAction = QtWidgets.QAction(MainWindow)
        self.quitAction.setObjectName("quitAction")
        self.contractNo = QtWidgets.QAction(MainWindow)
        self.contractNo.setCheckable(True)
        self.contractNo.setObjectName("contractNo")
        self.reportIssueAction = QtWidgets.QAction(MainWindow)
        self.reportIssueAction.setObjectName("reportIssueAction")
        self.openDocsAction = QtWidgets.QAction(MainWindow)
        self.openDocsAction.setObjectName("openDocsAction")
        self.remindTAFAction = QtWidgets.QAction(MainWindow)
        self.remindTAFAction.setCheckable(True)
        self.remindTAFAction.setObjectName("remindTAFAction")
        self.remindTrendAction = QtWidgets.QAction(MainWindow)
        self.remindTrendAction.setCheckable(True)
        self.remindTrendAction.setObjectName("remindTrendAction")
        self.remindSIGMETAction = QtWidgets.QAction(MainWindow)
        self.remindSIGMETAction.setCheckable(True)
        self.remindSIGMETAction.setObjectName("remindSIGMETAction")
        self.warnTAFAction = QtWidgets.QAction(MainWindow)
        self.warnTAFAction.setCheckable(True)
        self.warnTAFAction.setObjectName("warnTAFAction")
        self.checkUpgradeAction = QtWidgets.QAction(MainWindow)
        self.checkUpgradeAction.setObjectName("checkUpgradeAction")
        self.postMenu.addAction(self.tafAction)
        self.postMenu.addAction(self.trendAction)
        self.postMenu.addAction(self.sigmetAction)
        self.postMenu.addSeparator()
        self.postMenu.addAction(self.quitAction)
        self.contractsMenu.addAction(self.contractNo)
        self.settingMenu.addAction(self.warnTAFAction)
        self.settingMenu.addAction(self.contractsMenu.menuAction())
        self.settingMenu.addSeparator()
        self.settingMenu.addAction(self.settingAction)
        self.helpMenu.addAction(self.openDocsAction)
        self.helpMenu.addAction(self.reportIssueAction)
        self.helpMenu.addAction(self.checkUpgradeAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutAction)
        self.menuBar.addAction(self.postMenu.menuAction())
        self.menuBar.addAction(self.settingMenu.menuAction())
        self.menuBar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(2)
        self.quitAction.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.recentTab), _translate("MainWindow", "RECENT"))
        item = self.tafTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "类型"))
        item = self.tafTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "报文内容"))
        item = self.tafTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "发布时间"))
        item = self.tafTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "查询"))
        item = self.tafTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "其他"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tafTab), _translate("MainWindow", "TAF"))
        item = self.metarTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "类型"))
        item = self.metarTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "报文内容"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.metarTab), _translate("MainWindow", "METAR"))
        self.postMenu.setTitle(_translate("MainWindow", "编发"))
        self.settingMenu.setTitle(_translate("MainWindow", "选项"))
        self.contractsMenu.setTitle(_translate("MainWindow", "联系人"))
        self.helpMenu.setTitle(_translate("MainWindow", "帮助"))
        self.tafAction.setText(_translate("MainWindow", "预报"))
        self.trendAction.setText(_translate("MainWindow", "趋势"))
        self.sigmetAction.setText(_translate("MainWindow", "重要气象情报"))
        self.settingAction.setText(_translate("MainWindow", "设置"))
        self.aboutAction.setText(_translate("MainWindow", "关于"))
        self.quitAction.setText(_translate("MainWindow", "退出"))
        self.contractNo.setText(_translate("MainWindow", "无"))
        self.reportIssueAction.setText(_translate("MainWindow", "报告问题"))
        self.openDocsAction.setText(_translate("MainWindow", "文档"))
        self.remindTAFAction.setText(_translate("MainWindow", "预报"))
        self.remindTrendAction.setText(_translate("MainWindow", "趋势预报"))
        self.remindSIGMETAction.setText(_translate("MainWindow", "重要气象情报"))
        self.warnTAFAction.setText(_translate("MainWindow", "告警"))
        self.checkUpgradeAction.setText(_translate("MainWindow", "检查更新"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

