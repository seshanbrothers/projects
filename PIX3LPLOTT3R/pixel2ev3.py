#!/usr/bin/python
# -*- coding: utf-8 -*- import python packages



#install --> (sudo) apt-get install python-pip --> (sudo) pip install pillow termcolor python-ev3dev
#running --> run (sudo) python pythonfilename.py imagefilename.png (jpg will work along with others types) -->
#            you will be given a dialogue --> just type "" and return/enter to continue --> when presented with a color dialogue swap pen to that color
#errors --> try using (r,g,b = ...) instead of (r,g,b,a = ...) ***EVERYWHERE BELOW**

from PIL import Image, ImageFilter
from termcolor import colored
import time
import os
import sys


# paper resolution
horiz_deg = 1950; #degress max move
horiz_width = 6; #inches
horiz_res = horiz_deg/horiz_width-10; # degrees per inch
vertical_deg = -17000; #degress max move
vertical_width = 6.5; #inches
vertical_res = vertical_deg/vertical_width; # degrees per inch
vert_move = 15;
horiz_move = vert_move*horiz_res/vertical_res;
res = 140;
bottom = 1700
horiz_move = 15;

filename = sys.argv[1]

w = 0
h = 0
l = 0
img2 = Image.open(filename) #open image
img=img2.convert("RGBA")
width, height = img.size # get image size

sys.stdout.write(filename)
sys.stdout.write('\r')
sys.stdout.write(str(width))
sys.stdout.write('\r')
sys.stdout.write(str(height))
sys.stdout.write('\r')

#different colors: (in rgba -- remove last number in set to convert to rgb)
#red = (255,0,0,0) eg. in rgb -- (255,0,0)
#green = (0,255,0,0)
#blue = (0,0,255,0)
#black = (0,0,0,0)
#white = (255,255,255,0)

w = 0 #define starting width counter
while h != height:
        while w != width:
            #get rgba black or white of each pixel and write to full array
            #array.append(img.getpixel((w, h))) 
            #get rgba of each pixel
            r,g,b,a = img.getpixel((w, h)) 
            #check if red, green, or blue is greatest in rgb values
            # --- check if black or white also --> then append
            #array differently for each switch case
            if r > g and r > b :
                # print colored("█","red"),
                sys.stderr.write("r")
                sys.stdout.write("r")
            elif g > r and g > b :
                # print colored("█","green"), #print block if black pixel
                sys.stderr.write("g")
                sys.stdout.write("g")
            elif b > r and b > g :
                # print colored("█","blue"), 
                sys.stderr.write("b")
                sys.stdout.write("b")
            elif b < 50 and r < 50 and g < 50 :
                # print " ", #if terminal background is not black print block here instead
                sys.stderr.write("d")
                sys.stdout.write("d")
            else:
                # print "█", #if terminal background is not black print a space here instead
                sys.stderr.write(".")
                sys.stdout.write(".") #if terminal background is not black print a space here instead
            w = w+1 #move to next pixel -- use -1 to flip image -> make images not backward when printed
            sys.stdout.write('\r')
            
        sys.stderr.write('\n\r')
        w = 0 #reset width counter
        h = h+1 #move to next row



