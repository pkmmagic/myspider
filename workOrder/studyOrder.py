# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studyOrder.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 287)
        icon = QtGui.QIcon.fromTheme("start")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 23))
        self.menubar.setObjectName("menubar")
        self.menustart = QtWidgets.QMenu(self.menubar)
        self.menustart.setObjectName("menustart")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.menustart.addAction(self.actionStart)
        self.menustart.addAction(self.actionRestart)
        self.menustart.addSeparator()
        self.menustart.addAction(self.actionExit)
        self.menubar.addAction(self.menustart.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionStart.triggered.connect(self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Order"))
        MainWindow.setStatusTip(_translate("MainWindow", "Focus, man"))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.menustart.setTitle(_translate("MainWindow", "Option"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionRestart.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Click to Exit"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStart.setShortcut(_translate("MainWindow", "Alt+E"))

