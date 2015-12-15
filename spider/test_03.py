__author__ = 'joe'
import urllib2
from urllib import *

url = 'http://www.hupu.com/'
values = {'name': 'why',
          'location': 'SDU',
          'language': 'python'}
data = urlencode(values)
# print data -->name=why&language=python&location=SDU
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
html = response.read()
print html
