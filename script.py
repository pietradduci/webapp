#!/usr/bin/python
import os,sys
import cgi
import cgitb; cgitb.enable()

# set HOME environment variable to a directory the httpd server can write to
os.environ[ 'HOME' ] = '.'

import matplotlib
# chose a non-GUI backend
matplotlib.use( 'Agg' )

import pylab

#Deals with inputing data into python from the html form
form = cgi.FieldStorage()

# construct your plot
pylab.plot([1,2,3])

print "Content-Type: image/png\n"

# save the plot as a png and output directly to webserver
pylab.savefig( "tempfile.png", format='png' )
import shutil
shutil.copyfileobj(open("tempfile.png",'rb'), sys.stdout)