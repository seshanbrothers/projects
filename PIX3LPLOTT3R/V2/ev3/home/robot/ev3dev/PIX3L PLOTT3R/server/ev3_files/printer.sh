#!/bin/bash
#using default password (maker) and defalt user (robot)
cd projects/PIX3L\ PLOTT3R #change dir to cloned git repo
echo 'maker' | sudo -S python printweb.py "/home/robot/$1" #start print with specified image
