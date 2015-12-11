from Tkinter import *

class pic_window:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)
	top.geometry("150x100+1000+500")

        b = Button(top, text="Take Picture!", command=self.ok)
        b.grid(row =0, column=0)

    def ok(self):

        self.top.destroy()
