from Tkinter import *

class user_frame(Frame):
	def __init__(self, parent, **options):
		Frame.__init__(self, parent, **options)
		self.test = Label(self, text = 'hello world')
		self.test.grid(row=0, column=0)