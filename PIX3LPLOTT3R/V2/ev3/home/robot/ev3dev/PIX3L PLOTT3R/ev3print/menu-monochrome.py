#!/usr/bin/env python

import array
import fcntl
import sys
import os
# from linux/input.h

KEY_UP = 103
KEY_DOWN = 108
KEY_LEFT = 105
KEY_RIGHT = 106
KEY_ENTER = 28
KEY_BACKSPACE = 14
keys = [] 
KEY_MAX = 0x2ff
i = 0
menu = []
import glob
os.chdir("/home/sanjay/monochrome")
for file in glob.glob("*.*"):
    print(file)
    menu.append(file)
#menu = ['mona','scream','girl']
def EVIOCGKEY(length):
    return 2 << (14+8+8) | length << (8+8) | ord('E') << 8 | 0x18

# end of stuff from linux/input.h

BUF_LEN = (KEY_MAX + 7) / 8

def test_bit(bit, bytes):
    # bit in bytes is 1 when released and 0 when pressed
    return not bool(bytes[bit / 8] & (1 << (bit % 8)))

def main():
    buf = array.array('B', [0] * BUF_LEN)
    with open('/dev/input/by-path/platform-gpio-keys.0-event', 'r') as fd:
        ret = fcntl.ioctl(fd, EVIOCGKEY(len(buf)), buf)

    if ret < 0:
        print "ioctl error", ret
        sys.exit(1)
    global i
    for key in ['UP', 'DOWN', 'LEFT', 'RIGHT', 'ENTER', 'BACKSPACE']:
        key_code = globals()['KEY_' + key]
	key_state = test_bit(key_code, buf) and "pressed" or "released"
	keys.append(key_state)
	x = 0
        print '%9s : %s' % (key, key_state)
	while x != 1:
	    buf = array.array('B', [0] * BUF_LEN)
	    with open('/dev/input/by-path/platform-gpio-keys.0-event', 'r') as fd:
      	 	 ret = fcntl.ioctl(fd, EVIOCGKEY(len(buf)), buf)

 	    if ret < 0:
        	print "ioctl error", ret
        	sys.exit(1)
            key_code = globals()['KEY_' + key]
	    key_state = test_bit(key_code, buf) and "pressed" or "released"
            print '%9s : %s' % (key, key_state)
	    if key_state == "released":
			x = 1
#    print(len(keys))
    if keys[0] == "pressed" and i < len(menu)-1:
	i = i+1	
    if keys[4] == "pressed":
        os.system('python /home/sanjay/ev3print/printmonochrome.py '+menu[i]+' > /dev/tty0')
    if keys[1] == "pressed" and  i > -1:
        i = i-1
    os.system('echo  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" > /dev/tty0')
    os.system('echo '+menu[i]+' > /dev/tty0')
    global keys
    keys = []
   
while True:
	if __name__ == "__main__":
    		main()
