#!/usr/bin/python
# -*- coding: utf-8 -*- import python packages
#This code DOES NOT wait for user dialogue
#install --> (sudo) apt-get install python-pip --> (sudo) pip install pillow python-ev3dev
#running --> run (sudo) python pythonfilename.py imagefilename.png (jpg will work along with others types) -->

from PIL import Image, ImageFilter

import time

import os
import sys

# paper resolution
horiz_deg = -1800; #degress max move
horiz_width = 5; #inches
horiz_res = horiz_deg/horiz_width; # degrees per inch
vertical_deg = 850; #degress max move
vertical_width = 6.5; #inches
vertical_res = vertical_deg/vertical_width; # degrees per inch
vert_move = 7;
horiz_move = vert_move*horiz_res/vertical_res;
res = horiz_deg/horiz_move/1.1;


#resise and flip image
filename = sys.argv[1]
#cmd = "convert " + filename + " -threshold 90% -flop -resize " + str(res) + " print.jpg"
cmd = "convert " + filename + " -flatten  print.jpg"
#cmd = "cp "+filename+" print.jpg"
os.system(cmd) #execute command
image_file = Image.open('print.jpg') # open image print.jpg in current directory
image_file = image_file.convert('1') # convert image to pure black and white (just in case image is greyscale or color)
image_file.save('print.png') # save b&w image

w = 0
h = 0
l = 0
img = Image.open('print.png') #open black and white image
width, height = img.size # get image size
array = []
print width," x ", height
while h < height:
        while w < width:
                array.append(img.getpixel((w, h))) #get black or white of each pixel
                if img.getpixel((w, h)) != 255: #is pixel black?
                        print "█", #print block if black pixel
                else:
                        print " ",
                w = w+8 #move to next pixel
        w = 0 #reset width counter
        h = h+8 #move to next row
        print(" ")
all_pixels = array #save array of pixels to all_pixels



