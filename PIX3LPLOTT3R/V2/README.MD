# Pix3l Plott3r code using ev3dev

<b> What is ev3dev and linux</b>

Linux is the kernel that runs on many devices. Linux is used by the ev3, raspberry pi and ordinary PCs through an operating system, such as Debian, EV3 Firmware, Ubuntu, etc.

Ev3dev is Debian GNU/Linux for your ev3. This allows you to take advantage of certain ev3 features and program in other languages. Our code uses python.



<b>Installing our code</b>

Getting ev3dev:

** IT IS CRUCIAL THAT YOU DO NOT DOWNLOAD THE LATEST VERSION OF EV3DEV OR RUN UPGRADE. IF YOU DO THE CODE WILL NOT WORK ***

1) Download: https://github.com/ev3dev/ev3dev/releases/download/ev3dev-jessie-2015-12-30/ev3-ev3dev-jessie-2015-12-30.img.xz

2) Extract it using 7zip or another tool, until you are left with a file ending with .img

3) Follow Step 6 and 7 on this page: http://www.ev3dev.org/docs/getting-started/

Getting our code:

1) Run "sudo apt update ; sudo apt install git python-pip imagemagick"

2) Run "sudo pip install python-ev3dev termcolor pillow"

2) Run "git clone https://github.com/seshanbrothers/projects.git"

3) Run "cd projects/PIX3LPLOTT3R/V2/ev3/"

4) Run "sudo cp -rv * /"


Testing your installation:

1) Run "cd ~/ev3dev/PIX3L\ PLOTT3R"

2) Run "sudo python printmonochrome.py 'sample\ images/monochrome/LEGO.jpg'"

2a) Follow all dialogue printed on screen and when a question is asked, type in two quotes ("") and press return/enter on your keyboard 

3) (Optional) To print in color, run "sudo python printcolor.py 'sample\ images/color/EV3Logo.png'"

3a) Follow all dialogue printed on screen. When a color name is printed on your screen, change your pen to the corresponding color. When a pen is switched or a question is asked, type in two quotes ("") and press return/enter on your keyboard 




OPTIONAL - Running a server on a Raspberry Pi running Debian (or a derivitive such as Ubuntu or Raspbian):

*** Your username must be "pi" and the password "raspberry" for the code to work ****

*   Prerequisites:
*   
        sudo apt-get update
        sudo apt-get install apache2 sshpass php5 libapache2-mod-php5 php5-mcrypt iceweasel git


*   Download this folder:

1)        git clone https://github.com/seshanbrothers/projects.git

2)        cd projects/PIX3LPLOTT3R/V2/pc_files

3)        sudo cp -r * /


You will need to replace <code>192.168.43.22</code> in sendprint.py with the ev3's ip address

Run:

1) sed -i 's/192.168.43.22/YOUR_EV3_IP_HERE/g' sendprint.py

*   Run Code:
  
        cd ~/
        mkdir files
        mkdir lock
        python printer.py &
        python sendprint.py & 
        Go to http://localhost/ in Firefox/Iceweasel

