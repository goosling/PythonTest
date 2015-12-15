__author__ = 'joe'

import Tkinter

top = Tkinter.Tk()
label = Tkinter.Label(top, text = 'Hello World')
label.pack()

quit = Tkinter.Button(top, text='QUIT', command=top.quit,
                      bg='red', fg='white')
quit.pack(fill=Tkinter.X, expand=1)


Tkinter.mainloop()