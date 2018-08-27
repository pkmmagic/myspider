from tkinter import *
import tkinter.messagebox as messagebox

import random

a = [x for x in range(1,9)]

random.shuffle(a)


def sort(b):

    for i in range(7):
        if i<6 and b[i]>5 and b[i+1]>5 and b[i+2]>5:
            b[i+1], b[(i+4)%8] = b[(i+4)%8],b[i+1]

        elif b[6]>5 and b[7]>5 and b[1]>5:
            b[7],b[3] = b[3], b[7]
            
        elif b[i]>5 and b[i+1]>5:
            b[i+1], b[(i+2)%8] = b[(i+2)%8],b[i+1]
    return b

sort(a)



class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()


    def hello(self):
        name = self.nameInput.get()
        messagebox.showinfo('Message', str(a[int(name)]))#'Hello, %s' % name)
        

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
