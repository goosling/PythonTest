__author__ = 'joe'

# !/usr/bin/env python

from Tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % \
        scale.get())
top = Tk()
# where the window show
top.geometry('400x150')
label = Label(top, text='HelloWorld',
              font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)

scale = Scale(top, from_=1, to=40, orient=HORIZONTAL, command=resize)
scale.set(15)
scale.pack(fill=X, expand=1)

quit = Button(top, text='QUIT', command=top.quit,
              activeforeground='white', activebackground='red')
quit.pack()

mainloop()