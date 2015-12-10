from Tkinter import *
from pytesser import image_to_string
from PIL import Image, ImageFilter, ImageEnhance, ImageTk
import picamera
from datetime import datetime
from pic_window import pic_window

class user_frame(Frame):
	def __init__(self, parent, **options):
		Frame.__init__(self, parent, **options)

		self.balance = str(-1)
		self.name = None;
		self.security_pic = None
		self.deposit_amount = 0

		self.camera = picamera.PiCamera()
		
		self.__setup_button_frame()
		self.__setup_withdraw_frame()
		self.__setup_deposit_frame()
		self.__setup_picture_frame()

		#this is essentially an empty frame as a placeholder
		self.action_frame = Frame(self)
		self.action_frame.grid(row = 0, column =1, sticky = N+S+E+W)
		
		Grid.grid_columnconfigure(self, 0, weight = 1)
		Grid.grid_columnconfigure(self, 1, weight = 1)
		Grid.grid_rowconfigure(self, 0, weight = 1)
	
	def update_balance(self, val):
		self.balance = str(val)
		self.balance_l.config(text = "Balance: $"+self.balance)

	def update_name(self, name):
		self.name = name

	def update_sec_pic(self, img):
		self.security_pic = img
		self.pf_pic_label.config(image = img)

	##TODO: implement all these functions 
	##from parnter implementations
	def withdraw_action(self):
		print 'withdrawing!'
		withdraw_amount = self.wf_amount_entry.get()


	def deposit_action(self):
		print 'depositing '+self.deposit_amount

	def save_sec_pic_action(self):
		print 'saving security pic'

		#send request to update security pic


	def check_picture_action(self):
		print 'taking picture of check'
		time = str(datetime.now())

		
		self.camera.start_preview(fullscreen = False, window=(100, 20, 640, 480))
		
		waiter = pic_window(self)
		self.wait_window(waiter.top)

		self.camera.capture(time+'.jpg')
		self.camera.stop_preview()

		im = Image.open(time+".jpg")
		text = image_to_string(im)
		im = im.resize((480, 270), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(im)

		self.df_pic_label.config(image = photo)
		self.df_pic_label.photo = photo

		print text.rstrip()
		try:
			self.deposit_amount = float(text.rstrip())
			self.df_value_label.config("$"+self.deposit_amount+" detected")
		except:
			self.df_value_label.config(text="No money detected")


	def security_picture_action(self):
		print 'taking security picture'
		time = str(datetime.now())

		self.camera.start_preview(fullscreen = False, window=(100, 20, 640, 480))
		
		waiter = pic_window(self)
		self.wait_window(waiter.top)
		
		self.camera.capture(time+'.jpg')
		self.camera.stop_preview()

		self.security_pic = Image.open(time+".jpg")
		im = im.resize((480, 270), Image.ANTIALIAS)
		photo = ImageTk.PhotoImage(im)
		self.pf_pic_label.config(image = photo)
		self.pf_pic_label.photo = photo

	def set_withdraw_frame(self):
		self.action_frame.grid_remove()
		self.deposit_frame.grid_remove()
		self.picture_frame.grid_remove()
		self.withdraw_frame.grid(row = 0, column =1, sticky = N+S+E+W)
		self.deposit_b.config(state = ACTIVE)
		self.picture_b.config(state = ACTIVE)
		self.withdraw_b.config(state = DISABLED)	

	def set_deposit_frame(self):
		self.action_frame.grid_remove()
		self.withdraw_frame.grid_remove()
		self.picture_frame.grid_remove()
		self.deposit_frame.grid(row = 0, column =1, sticky = N+S+E+W)
		self.deposit_b.config(state = DISABLED)
		self.picture_b.config(state = ACTIVE)
		self.withdraw_b.config(state = ACTIVE)

	def set_picture_frame(self):
		self.action_frame.grid_remove()
		self.deposit_frame.grid_remove()
		self.withdraw_frame.grid_remove()
		self.picture_frame.grid(row = 0, column =1, sticky = N+S+E+W)
		self.deposit_b.config(state = ACTIVE)
		self.picture_b.config(state = DISABLED)
		self.withdraw_b.config(state = ACTIVE)

	def __setup_withdraw_frame(self):
		self.withdraw_frame = Frame(self)

		self.wf_amount_label = Label(self.withdraw_frame, 
			text = 'Amount:',
			font = ('Corbel', '16'))
		self.wf_amount_label.grid(row = 0, column = 0, 
			padx = 10, pady =10, sticky = E)

		self.wf_amount_entry = Entry(self.withdraw_frame, 
			font = ('Corbel', '16'))
		self.wf_amount_entry.grid(row = 0, column = 1, 
			padx = 10, pady =10, sticky = W)

		self.wf_go_button = Button(self.withdraw_frame, text = 'GO',
			font = ('Corbel', '16'), command = self.withdraw_action)
		self.wf_go_button.grid(row = 1, column = 0, columnspan = 2)

		Grid.grid_columnconfigure(self.withdraw_frame, 0, weight = 1)
		Grid.grid_rowconfigure(self.withdraw_frame, 0, weight = 1)
		Grid.grid_columnconfigure(self.withdraw_frame, 1, weight = 1)
		Grid.grid_rowconfigure(self.withdraw_frame, 1, weight = 1)

	def __setup_deposit_frame(self):
		self.deposit_frame = Frame(self)

		self.df_take_pic_button = Button(self.deposit_frame, 
			text = 'Take Picture', 
			font = ('Corbel', '16'), 
			command = self.check_picture_action)
		self.df_take_pic_button.grid(row = 0, column = 0)

		self.df_pic_label = Label(self.deposit_frame,
			image = self.security_pic)
		self.df_pic_label.grid(row = 1, column =0)
		self.df_pic_label.photo = None

		self.df_value_label = Label(self.deposit_frame, 
			text = 'No money detected.', 
			font = ('Corbel', '16'))
		self.df_value_label.grid(row = 2, column = 0)

		self.df_deposit_button = Button(self.deposit_frame,
			text = 'Deposit', 
			font = ('Corbel', '16'), 
			command = self.deposit_action)
		self.df_deposit_button.grid(row = 3, column = 0)

		Grid.grid_rowconfigure(self.deposit_frame, 0, weight = 1)
		Grid.grid_columnconfigure(self.deposit_frame, 0, weight = 1)
		Grid.grid_columnconfigure(self.deposit_frame, 1, weight = 1)
		Grid.grid_columnconfigure(self.deposit_frame, 2, weight = 1)
		Grid.grid_columnconfigure(self.deposit_frame, 3, weight = 1)


	def __setup_picture_frame(self):
		self.picture_frame = Frame(self)

		self.pf_take_pic_button = Button(self.picture_frame, 
			text = 'Take Picture', 
			font = ('Corbel', '16'), 
			command = self.security_picture_action)
		self.pf_take_pic_button.grid(row = 0, column = 0)

		self.pf_pic_label = Label(self.picture_frame,
			image = self.security_pic, text = 'pic goes here')
		self.pf_pic_label.grid(row = 1, column =0)
		self.pf_pic_label.photo = None

		self.pf_deposit_button = Button(self.picture_frame,
			text = 'Save', 
			font = ('Corbel', '16'), 
			command = self.save_sec_pic_action)
		self.pf_deposit_button.grid(row = 3, column = 0, padx = 15, pady = 15)

		Grid.grid_rowconfigure(self.picture_frame, 0, weight = 1)
		Grid.grid_columnconfigure(self.picture_frame, 0, weight = 1)
		Grid.grid_columnconfigure(self.picture_frame, 1, weight = 1)
		Grid.grid_columnconfigure(self.picture_frame, 2, weight = 1)


	def __setup_button_frame(self):
		self.button_frame = Frame(self)
		self.button_frame.grid(row = 0, column = 0, sticky = N+S+E+W)
		
		self.balance_l = Label(self.button_frame, 
			text = "Balance: $"+self.balance, font = ('Corbel', '16'))
		self.balance_l.grid(row = 0, column = 0)

		self.withdraw_b = Button(self.button_frame, width = 20, 
			font = ('Corbel', '16'), 
			text = "Withdraw...", 
			command = self.set_withdraw_frame)
		self.withdraw_b.grid(row=1, column=0)

		self.deposit_b = Button(self.button_frame, width = 20, 
			font = ('Corbel', '16'), 
			text = "Deposit...", 
			command = self.set_deposit_frame)
		self.deposit_b.grid(row=2, column=0)

		self.picture_b = Button(self.button_frame, width = 20,
			font = ('Corbel', '16'),
			text = "Take Security Picture...",  
			command = self.set_picture_frame)
		self.picture_b.grid(row=3, column=0)

		Grid.grid_columnconfigure(self.button_frame, 0, weight = 1)
		Grid.grid_rowconfigure(self.button_frame, 0, weight = 1)
		Grid.grid_rowconfigure(self.button_frame, 1, weight = 1)
		Grid.grid_rowconfigure(self.button_frame, 2, weight = 1)
		Grid.grid_rowconfigure(self.button_frame, 3, weight = 1)

