import time
import ui
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import myspider

downloadPath = r'D:\aQuand\10\\'
mainPage = 'www.weiai2048.com'
libPath = 'lib.txt'
libIndex = 4500
pace = 500
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': 'a22e7_lastvisit=112%091535505414%09%2F2048%2Fread.php%3Ftid-277185.html; a22e7_lastpos=T277185; a22e7_threadlog=%2C27%2C; a22e7_ol_offset=181487; visid_incap_1639104=SekGbbI1QoC/bXYwjTedTikLcVsAAAAAQUIPAAAAAACkHhHDMrj7ftVbmx02YxtJ; a22e7_readlog=%2C277185%2C; __tins__19410549=%7B%22sid%22%3A%201535505438336%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201535507238336%7D; __51cke__=; __51laig__=1'
}
num_list = myspider.get_num_list(libPath)
num_list = sorted(num_list)[libIndex: (pace + libIndex)]

class RunThread(QtCore.QThread):
    counter_value = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, counter_start=0):
        super(RunThread, self).__init__(parent)
        self.counter = int(counter_start*pace/100)
        self.is_running = True

    def go(self, num):
        try:
            myspider.thread_num(num, downloadPath, mainPage, headers)
            ind = num_list.index(num) + 1
            tot = len(num_list)
        except Exception as e:
            print(e)

    def run(self):
        while self.counter<pace and self.is_running == True:
            num = num_list[self.counter]
            self.go(num)
            self.counter+=1
            self.counter_value.emit(int((self.counter/len(num_list))*100))

    def stop(self):
        self.is_running = False
        print('stopping thread')
        self.terminate()

class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.update_progressbar()
        MainWindow.show()
        sys.exit(app.exec_())

    def update_progressbar(self):
        self.ui.radioButton.clicked.connect(self.start_progressbar)
        self.ui.radioButton_2.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_3.clicked.connect(self.reset_progressbar)

    def progressbar_counter(self, start_value=0):
        self.run_thread = RunThread(parent=None, counter_start = start_value)
        self.run_thread.start()
        self.run_thread.counter_value.connect(self.set_progressbar)

    def set_progressbar(self, counter):
        if not self.stop_progress:
            self.ui.progressBar.setValue(counter)

    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.ui.progressBar.value()
        self.progressbar_counter(self.progress_value)

    def stop_progressbar(self):
        self.stop_progress = True
        try:
            self.run_thread.stop()
        except:
            pass

    def reset_progressbar(self):
        self.progress_value = 0
        self.ui.progressBar.reset()
        self.stop_progress = False


if __name__ == "__main__":
    MainWindow()
