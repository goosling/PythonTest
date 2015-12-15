__author__ = 'joe'

# !/usr/bin/env python

import urllib2
from urlparse import urlparse as up
from base64 import encodestring

LOGIN = 'wesc'
PASSWD = 'you will never guess'
URL = 'http://localhost'

def handler_version(url):
    hdlr = urllib2.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', up(url)[1], LOGIN, PASSWD)
    opener = urllib2.build_opener(hdlr)
    urllib2.install_opener(opener)
    return url

def request_version(url):
    req = urllib2.Request(url)
    b64str = encodestring('%s:%s' % (LOGIN, PASSWD))[:-1]
    req.add_header('Authorization', 'Basic %s' % b64str)
    return req

for funType in ('handler', 'request'):
    print '*** Using %s:' % funType.upper()
    url = eval('%s_version')(URL)
    f = urllib2.urlopen(url)
    print f.readline()

    f.close()
