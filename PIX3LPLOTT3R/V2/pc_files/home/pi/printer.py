import os, time
import glob
l = 0
z = 0
ip = "192.168.1.9"
path_to_watch = "/var/www/html/uploads/"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (2)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
#  if added: print "Added: ", ", ".join (added)
  if added:
    x=0
    while x != len(added):
	    z = z+1
	    print added[x]
	    name = added[x].split('_')[1]
	    os.system('echo "'+added[x]+'" > files/'+str(z*3)+'_'+name+'.txt')
	    save = added[x]
#            os.system('mv "Downloads/'+added[x]+'" Downloads/print.png')
            added[x] = 'print.png'
            added[x] = added[x].replace (" ", "\ ")
	    x = x + 1
  before = after
