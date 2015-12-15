__author__ = 'joe'

import urllib2

req = urllib2.Request('http://www.hupu.com/')
response = urllib2.urlopen(req)
html = response.read()
print html
