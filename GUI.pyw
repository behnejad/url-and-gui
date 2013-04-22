# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Apr 22 09:46:29 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(608, 430)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.adressbar = QtGui.QLineEdit(self.centralwidget)
        self.adressbar.setGeometry(QtCore.QRect(10, 10, 481, 20))
        self.adressbar.setObjectName(_fromUtf8("adressbar"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.search = QtGui.QGroupBox(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(20, 50, 571, 91))
        self.search.setObjectName(_fromUtf8("search"))
        self.Day = QtGui.QLineEdit(self.search)
        self.Day.setGeometry(QtCore.QRect(40, 20, 111, 21))
        self.Day.setObjectName(_fromUtf8("Day"))
        self.label_day = QtGui.QLabel(self.search)
        self.label_day.setGeometry(QtCore.QRect(10, 20, 46, 21))
        self.label_day.setObjectName(_fromUtf8("label_day"))
        self.label_month = QtGui.QLabel(self.search)
        self.label_month.setGeometry(QtCore.QRect(190, 20, 46, 21))
        self.label_month.setObjectName(_fromUtf8("label_month"))
        self.Month = QtGui.QLineEdit(self.search)
        self.Month.setGeometry(QtCore.QRect(230, 20, 113, 20))
        self.Month.setObjectName(_fromUtf8("Month"))
        self.label_year = QtGui.QLabel(self.search)
        self.label_year.setGeometry(QtCore.QRect(400, 20, 46, 21))
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.Year = QtGui.QSpinBox(self.search)
        self.Year.setGeometry(QtCore.QRect(430, 20, 81, 22))
        self.Year.setMinimum(2000)
        self.Year.setMaximum(2013)
        self.Year.setObjectName(_fromUtf8("Year"))
        self.Search = QtGui.QPushButton(self.search)
        self.Search.setGeometry(QtCore.QRect(10, 60, 551, 23))
        self.Search.setObjectName(_fromUtf8("Search"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 160, 581, 211))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 608, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),MainWindow,self.salam)

    def salam():
        print self.adressbar.text()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.adressbar.setStatusTip(_translate("MainWindow", "type your adress", None))
        self.pushButton.setText(_translate("MainWindow", "Go", None))
        self.search.setTitle(_translate("MainWindow", "Search", None))
        self.Day.setStatusTip(_translate("MainWindow", "Day", None))
        self.label_day.setText(_translate("MainWindow", "Day", None))
        self.label_month.setText(_translate("MainWindow", "Month", None))
        self.Month.setStatusTip(_translate("MainWindow", "Month", None))
        self.label_year.setText(_translate("MainWindow", "Year", None))
        self.Year.setStatusTip(_translate("MainWindow", "Year", None))
        self.Search.setStatusTip(_translate("MainWindow", "Search", None))
        self.Search.setText(_translate("MainWindow", "Search", None))
        self.textBrowser.setStatusTip(_translate("MainWindow", "News", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit Application", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About Application", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

