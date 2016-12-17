<h1>PIX3L PLOTT3R Menu System to Select File</h1>
<img src="https://scontent-iad3-1.xx.fbcdn.net/hphotos-xlt1/v/t1.0-9/12742519_1509710212669723_4304083322119299525_n.jpg?oh=b11d74b98a01d2f8db4a8b8aaad7529b&oe=57548740">
<b>
NOTE: These files are a WORK IN PROGRESS!
</b>

This code will print the menu system to the ev3 screen and will use the ev3 buttons. (Run from a computer not from Brickman)

We provide code to print in black & white and color.
We also provide sample images.

You will need to modify the code to accomidate the location of your files. The menu system should be run as root. (<code>su</code> --> Default password is <code>r00tme</code>)



*   Prerequisites:
*   
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install python-pip
        sudo pip install python-ev3dev termcolor pillow
	sudo service brickman stop

*   The ev3dev version should be the latest. To upgrade:

        sudo apt-get dist-upgrade


*   Download this folder:
*   
        sudo apt-get install git
        git clone https://github.com/droidsrobotics/ev3dev.git
        cd ev3dev/PIX3L\ PLOTT3R/ev3print

*   Run Black and White Menu System:
  
        python menu-monochrome.py

*   Run Color Code:

        python menu-color.py
        
The code will automatically scan for images in a set directory.
