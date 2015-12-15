__author__ = 'joe'
# -*- coding: utf-8 -*-

import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({'http': 'http://www.baidu.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

# 设置timeout参数
# response = urllib2.urlopen('http://www/google.com', timeout=10)
# 加入特定header
request = urllib2.Request('http://www.baidu.com/')
request.add_header('User-Agent', 'fake-client')
response = urllib2.urlopen(request)
print response.read()
