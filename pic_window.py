from Tkinter import *

class pic_window:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        b = Button(top, text="Take Pciture!", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        self.top.destroy()
