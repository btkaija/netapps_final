#added coment from pi
from Tkinter import *

class atm_client:
	def __init__(self):
		self.base_window = Tk()
		self.base_window.title('ATM Machine')
		
		self.__set_window_size()

		self.login_frame = Frame(self.base_window)
		self.login_frame.grid(row = 0, column = 0, sticky= N+S+E+W)
		self.login_logout = Button(self.base_window, text = 'Login', command = self.login_logout_press)
		self.login_logout.grid(row = 1, column = 0, sticky= N+S+E+W, padx = 25, pady = 25)
		self.logged_in = False

		self.user_label = Label(self.login_frame, text = 'User ID')
		self.user_label.grid(row=1, column=0)
		self.pass_label = Label(self.login_frame, text = 'Password')
		self.pass_label.grid(row=2, column=0)

		Grid.grid_columnconfigure(self.base_window, 0, weight = 1)
		Grid.grid_rowconfigure(self.base_window, 0, weight = 1)
		# Grid.grid_columnconfigure(self.base_window, 1, weight = 1)
		Grid.grid_rowconfigure(self.base_window, 1, weight = 1)

		self.base_window.mainloop()

	def login_logout_press(self):
		print "hello world"

	def __set_window_size(self):
		# print "Setting window size"
		width = self.base_window.winfo_screenwidth()
		height = self.base_window.winfo_screenheight()
		self.base_window.geometry(str(width-50)+'x'+str(height-75)+'+0+0')

client = atm_client()
