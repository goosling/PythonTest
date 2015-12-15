__author__ = 'joe'
# -*- coding: utf-8 -*-

import urllib2
import cookielib
'''
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com/')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
'''
'''
# debug log
httphandler = urllib2.HTTPHandler(debuglevel=1)
httpshandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httphandler, httpshandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.hupu.com/')
'''

# -*- coding: utf-8 -*-
import urllib
import urllib2
postdata = urllib.urlencode({
    'username': '汪小光',
    'password': 'why888',
    'continueURI': 'http://www.verycd.com/',
    'fk': '',
    'login_submit': '登录'
})
req = urllib2.Request(
    url='http://secure.verycd.com/signin',
    data=postdata
)
result = urllib2.urlopen(req)
print result.read()