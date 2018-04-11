#!/usr/bin/python
from commands import getstatusoutput
import cgi
print "Content-type:text/html\r\n\r\n"
form = cgi.FieldStorage() 
first_name = form.getvalue('firstname')
a=getstatusoutput('sudo /home/{0}'.format(first_name))
print a
