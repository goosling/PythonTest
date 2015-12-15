__author__ = 'joe'
# -*- coding: utf-8 -*-

import urllib
import re
import thread
import time
import urllib2

class Spider:
    def __init__(self):
        self.page = 1
        self.pages = []

        self.enable = False
    # 将所有的段子都抠出来，添加到列表中并返回列表
    def GetPage(self, page):
        myUrl = 'http://m.qiushibaike.com/hot/page/'+page
        user_agent = user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(myUrl, headers=headers)
        response = urllib2.urlopen(req)
        myPage = response.read()
        unicodePage = myPage.decode('utf-8')

        # 找出所有class='content'的div标记
        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>', unicodePage, re.S)
        items = []
        for item in myItems:
            # item中第一个div是标题，即时间
            # item中第二个div是内容
            items.append([item[0].replace('\n', ''), item[1].replace('\n', '')])
        return items

    #用于加载新的段子
    def loadPage(self):
        # 如果用户未输入quit则一直运行
        while self.enable:
            if len(self.pages) < 2:
                try:
                    myPage = self.getPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print '无法连接到糗百'
            else:
                time.sleep(1)
    def showPage(self, nowPage, page):
        for items in nowPage:
            print u'第%d页' % page, items[0], items[1]
            myInput = raw_input()
            if myInput == 'quit':
                self.enable = False
                break

    def start(self):
        self.enable = True
        page = self.page

        print u'正在加载请稍候。。。。'
        thread.start_new_thread(self.loadPage, ())

        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.showPage(nowPage, page)
                page += 1


print u'请按下回车浏览今日内容'
raw_input(' ')
myModel = Spider()
myModel.start()

