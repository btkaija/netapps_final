#added coment from pi
from Tkinter import *
from user_frame import user_frame
from PIL import Image, ImageTk


class atm_client:
	def __init__(self):
		self.base_window = Tk()
		self.base_window.title('ATM Machine')
		
		self.__set_window_size()
		self.__setup_login_frame()
		self.__setup_pic_secure_frame()

		self.user_data_frame = user_frame(self.base_window)


		self.login_logout = Button(self.base_window, text = 'Login',
			command = self.login_logout_press, width = 20, height = 3, 
			font = ('Corbel', '20', 'bold'))
		self.login_logout.grid(row = 1, column = 0, padx = 25, pady = 25)
		self.logged_in = False
		
		Grid.grid_columnconfigure(self.base_window, 0, weight = 1)
		Grid.grid_rowconfigure(self.base_window, 0, weight = 1)
		Grid.grid_rowconfigure(self.base_window, 1, weight = 1)

		self.base_window.mainloop()

	def login_logout_press(self):
		
		#when logging out
		if self.logged_in:
			#send logout request with pic

			self.user_data_frame.grid_remove()
			self.login_frame.grid(row = 0, column = 0, sticky = N+S+E+W)
			self.login_logout.config(state=ACTIVE, text = "Login")
			self.logged_in = False

		#when logging in
		else:
			self.user_name = self.user_entry.get()
			self.user_pass = self.pass_entry.get()


			#make login request and save balance to monies
			#and save picture to img
			img = Image.open("nick_cage.jpg")
			monies = 1000

			img = img.resize((480, 270), Image.ANTIALIAS)
			photo = ImageTk.PhotoImage(img)
			self.pic_label.photo = photo
			self.pic_label.config(image = photo)

			self.user_data_frame.update_balance(monies)
			self.user_data_frame.update_sec_pic(photo)
			self.user_data_frame.update_name(self.user_name)

			#end request
			self.login_frame.grid_remove()
			self.pic_secure_frame.grid(row = 0, column = 0, sticky = N+S+E+W)
			self.login_logout.config(state=DISABLED, text = "...")
			

	def confirm_pic_press(self):
		self.logged_in = True
		self.pic_secure_frame.grid_remove()

		self.user_data_frame.grid(row = 0, column = 0, sticky = N+S+E+W)
		self.login_logout.config(state=ACTIVE, text = "Logout")

	def deny_pic_press(self):
		#send logout request
		self.logged_in = False
		self.pic_secure_frame.grid_remove()

		self.login_frame.grid(row = 0, column = 0, sticky = N+S+E+W)
		self.login_logout.config(state=ACTIVE, text = "Login")


	def __set_window_size(self):
		# print "Setting window size"
		width = self.base_window.winfo_screenwidth()
		height = self.base_window.winfo_screenheight()
		self.base_window.geometry(str(width-50)+'x'+str(height-75)+'+0+0')

	def __setup_login_frame(self):
		self.login_frame = Frame(self.base_window)
		self.login_frame.grid(row = 0, column = 0, sticky= N+S+E+W)

		self.user_label = Label(self.login_frame, 
			text = "User's Name:", font = ('Corbel', '16'))
		self.user_label.grid(row=0, column=0, sticky = E+S, padx =10, pady = 10)
		self.pass_label = Label(self.login_frame, 
			text = 'Password:', font = ('Corbel', '16'))
		self.pass_label.grid(row=1, column=0, sticky = E+N, padx =10, pady = 10)

		self.user_entry = Entry(self.login_frame, font = ('Corbel', '16'))
		self.user_entry.grid(row=0, column=1, sticky = W+S, padx =10, pady = 10)
		self.pass_entry = Entry(self.login_frame, font = ('Corbel', '16'))
		self.pass_entry.grid(row=1, column=1, sticky = W+N, padx =10, pady = 10)

		Grid.grid_columnconfigure(self.login_frame, 0, weight = 1)
		Grid.grid_rowconfigure(self.login_frame, 0, weight = 1)
		Grid.grid_columnconfigure(self.login_frame, 1, weight = 1)
		Grid.grid_rowconfigure(self.login_frame, 1, weight = 1)


	def __setup_pic_secure_frame(self):
		self.pic_secure_frame = Frame(self.base_window)

		self.ask_pic_label = Label(self.pic_secure_frame, 
			font = ('Corbel', '16'), 
			text = 'Is this picture associated with your account?')
		self.ask_pic_label.grid(row = 0, column = 0, columnspan = 2)

		img = Image.open("nick_cage.jpg")
		img = img.resize((480, 270), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(img)
		#or use the one gotten from request

		self.pic_label = Label(self.pic_secure_frame, image = photo)
		self.pic_label.photo = photo
		self.pic_label.grid(row = 1, column = 0, 
			columnspan = 2, padx = 25, pady = 25)
		
		self.confirm_button = Button(self.pic_secure_frame, text = 'Confirm',
			command = self.confirm_pic_press, font = ('Corbel', '16'))
		self.confirm_button.grid(row = 2, column = 0, sticky = E, padx = 10)

		self.deny_button = Button(self.pic_secure_frame, text = 'Deny',
			command = self.deny_pic_press, font = ('Corbel', '16'))
		self.deny_button.grid(row = 2, column = 1, sticky = W, padx = 10)

		Grid.grid_columnconfigure(self.pic_secure_frame, 0, weight = 1)
		Grid.grid_rowconfigure(self.pic_secure_frame, 0, weight = 1)
		Grid.grid_columnconfigure(self.pic_secure_frame, 1, weight = 1)
		Grid.grid_rowconfigure(self.pic_secure_frame, 1, weight = 1)
		Grid.grid_rowconfigure(self.pic_secure_frame, 2, weight = 1)



client = atm_client()
