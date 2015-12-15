__author__ = 'joe'

# !/usr/bin/env python

import tkMessageBox
from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.namePut = Entry(self)
        self.namePut.pack()
        self.alterButton = Button(self, text='Hello', command=self.hello)
        self.alterButton.pack()

    def hello(self):
        name = self.namePut.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# app.master.title("Hello World")
app.mainloop()