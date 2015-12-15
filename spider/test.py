__author__ = 'joe'

import urllib2

req = urllib2.Request('http://www.baibai.com/')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    # print e.code
    # print e.reason
    if hasattr(e, 'code'):
        print 'the server could not fulfill the request '
        print 'Error code', e.code
    elif hasattr(e, 'reason'):
        print 'we failed to reach a server'
        print 'Reason', e.reason
    else:
        print 'no exception was raised'