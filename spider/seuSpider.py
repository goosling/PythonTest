__author__ = 'joe'
# -*- coding: utf-8 -*-

# 操作：输入学号和成绩
# 功能：输出绩点

import urllib2
import urllib
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

# 需要post数据
postdata = urllib.urlencode({
    'txt_user': '140989',
    'txt_password': '19910910'
})

# 自定义一个请求
req = urllib2.Request(
    url='http://202.119.4.150/nstudent/login.aspx',
    data=postdata
)

result = opener.open(req)

print result.read()