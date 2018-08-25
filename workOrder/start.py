# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import studyOrder, sys
import random

class MainWindow(object):
    global n, dic
    n = 0
    dic = ['Meditation', 'WUJUN', 'WZH', 'LXL', 'Fooled by R', 'WWG',
           'Python', 'Writing', 'XS', 'work', 'work']
    random.shuffle(dic)

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = studyOrder.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.getOrder()
        self.click_button()
        self.action_start()
        self.action_reset()
        MainWindow.show()
        sys.exit(app.exec_())

    def getOrder(self):
        global n, dic
        try:
            self.ui.label.setText(str(n + 1) + '\n' + dic[n])
            n += 1
        except:
            self.ui.label.setText('Restarting')
            n = 0
            random.shuffle(dic)


    def reSet(self):
        global n
        n = 0
        random.shuffle(dic)
        self.ui.label.setText('Restarted')

    def click_button(self):
        self.ui.pushButton.clicked.connect(self.getOrder)

    def action_start(self):
        self.ui.actionStart.triggered.connect(self.getOrder)

    def action_reset(self):
        self.ui.actionRestart.triggered.connect(self.reSet)



if __name__ == "__main__":
    MainWindow()
