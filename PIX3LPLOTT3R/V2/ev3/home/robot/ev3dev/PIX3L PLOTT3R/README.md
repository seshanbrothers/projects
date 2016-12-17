<h1>PIX3L PLOTT3R Project</h1>
<img src="https://scontent-iad3-1.xx.fbcdn.net/hphotos-xlt1/v/t1.0-9/12742519_1509710212669723_4304083322119299525_n.jpg?oh=b11d74b98a01d2f8db4a8b8aaad7529b&oe=57548740">

The robot can print from any image file using python!

We provide code to print in black & white and color.
We also provide sample images.

Note: The code only works with the 3.16.7-ckt21-9-ev3dev-ev3 linux kernel. You will have to convert the code to work with the latest version (linux ev3dev kernel 4.4.x).

*   Prerequisites:
*   
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install python-pip git imagemagick
        sudo pip install python-ev3dev termcolor pillow

*   The ev3dev version should be the latest. To upgrade:

        sudo apt-get dist-upgrade


*   Download this folder:
*   
        git clone https://github.com/droidsrobotics/ev3dev.git
        cd ev3dev/PIX3L\ PLOTT3R

*   Run Black and White Code:
  
        sudo python printmonochrome.py "sample\ images/monochrome/IMAGE_HERE.jpg"

*   Run Color Code:

        sudo python printcolor.py "sample\ images/color/IMAGE_HERE.png"
        
The color printing program will print 4 times with different pens. The code understands red, green, blue, and black and will automatically split images up into these colors. The file <code>printcolor-use-color-sensor.py</code> uses the color sensor to reset the paper position for each color.

When presented with a dialogue, type <code>" "</code> and press enter to continue. If the dialogue prints a color, switch the pen to that color, then continue. 


