#!/usr/bin/python
#Filename : backup_ver3.py

import os
import time

# 1. The files and directions to be backed up are specified in a list.
source = ['/home/xzy/python','/home/xzy/awk']

# 2. The backup must be stored in a main backup directory
target_dir = '/home/xzy/backup/' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name zip file
comment = raw_input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
  target = today + os.sep + now + '.zip'
else:  
  target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'
  # Notice the blackslash!

# Creat the subdirectory if it isn't already there
if not os.path.exists(today):
  os.mkdir(today) # make directory
  print 'Successful created directory', today

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
  print 'Successful backup to', target
else:
  print 'Backup FAILED'
