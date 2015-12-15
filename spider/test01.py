__author__ = 'joe'

import urllib2
response = urllib2.urlopen('http://www.hupu.com/')
html = response.read()
print html
