#!/usr/bin/python
from pytesser import *
from PIL import Image, ImageFilter, ImageEnhance
import picamera
from datetime import datetime

time = str(datetime.now())

camera = picamera.PiCamera()
camera.start_preview()
raw_input("Press Enter to continue...")
camera.capture(time+'.jpg')
camera.stop_preview()


im = Image.open(time+".jpg")
text = image_to_string(im)
print "text={}".format(text)
