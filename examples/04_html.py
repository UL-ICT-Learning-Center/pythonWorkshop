#!/usr/bin/python2

# retrieve a HTML page and print it using urllib2
# checkout other examples at http://docs.python.org/2/howto/urllib2.html

import urllib2
response = urllib2.urlopen('http://getbootstrap.com/examples/starter-template/')
html = response.read()
print( html )
