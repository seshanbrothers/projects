import glob,os,time
import os.path
from lockfile import LockFile
ip = "192.168.1.15"
username = "robot"
password = "maker"


while True:
  lock = LockFile("lock/lock")
  print "waiting for lock"
  lock.acquire()
  print "got lock"
  time.sleep(5)
  array = sorted(glob.glob("files/*.txt"))
  if array != []:
   print array[0]
   txt = open(''+array[0])
   txt = txt.read()
   os.system('rm '+array[0])
   lock.release()
   print "released and printing"
   print(txt)
   time.sleep(2)
   txt = txt.split('\n')[0]
   os.system('sshpass -p '+password+' scp "/var/www/html/uploads/'+txt+'" '+username+'@'+ip+':~/')
   os.system('sshpass -p '+password+' ssh -t '+username+'@'+ip+' "~/printer.sh \''+txt+'\'"')
   print "done"
