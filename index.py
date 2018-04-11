#!/usr/bin/python
from commands import getstatusoutput

print "Content-type:text/html\r\n\r\n"
print "<h1>Welcome to RH134 - SELinux Demo</h1>"
print """<form action='mkdir.py' method=post>
        Create Directory in /home/ :
  <input type="text" name="firstname" value="Mickey">
  <input type="submit" value="Submit">"""

