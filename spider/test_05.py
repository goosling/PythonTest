__author__ = 'joe'
# -*- coding: utf-8 -*-
import urllib2

# 创建一个密码管理者
psw_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# 添加用户名和密码
top_level_url = 'http://www.baidu.com/'

psw_mgr.add_password(None, top_level_url, 'why', '123')
# 创建一个新的handler
handler = urllib2.HTTPBasicAuthHandler(psw_mgr)
# 创建opener
opener = urllib2.build_opener(handler)

a_url = 'http://www.hupu.com/'

# 使用opener获取url
opener.open(a_url)

# 安装opener
urllib2.install_opener(opener)