__author__ = 'joe'
# -*- coding: utf-8 -*-

import string
import urllib2
import re

#处理页面上的各种标签
class HTML_Tool:
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    # 用非贪婪模式匹配任意<>标签
    EndCharToNoneRex = re.compile("<.*?>")
    # 用非贪婪模式匹配任意<p>标签
    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    # 将一些html符号实体变为原始符号
    replaceTab = [("<", "<"), (">", ">"), ("&", "&"), ("&", "\""), (" ", " ")]

    def repalce_char(self, x):
        x = self.BgnCharToNoneRex.sub("", x)
        x = self.BgnPartRex.sub('\n    ', x)
        x = self.CharToNewLineRex.sub('\n', x)
        x = self.CharToNextTabRex.sub('\t', x)
        x = self.EndCharToNoneRex.sub('', x)

        for t in self.replaceTab:
            x = x.replace(t[0], t[1])
        return x

class Baidu_Spider:
    def __init__(self, url):
            self.myUrl = url + '?see_lz=1'
            self.datas = []
            self.mytool = HTML_Tool()
            print u'已经启动百度贴吧爬虫'

    #初始化加载页面并将其转码储存
    def baidu_tieba(self):
        myPage = urllib2.urlopen(self.myUrl).read().decode('utf-8')
        endPage = self.page_counter(myPage)
        title = self.find_title(myPage)
        print u'文章名称：'+ title

        self.save_data(self.myUrl, title, endPage)
    def page_counter(self, myPage):
        myMatch = re.search(r'class="red">(\d+?)</span>', myPage, re.S)
        if myMatch:
            endPage = int(myMatch.group(1))
            print u'报告：发现楼主有%d页原创内容'% endPage
        else:
            endPage = 0
            print u'报告：无法计算楼主发布内容'
        return endPage

    def title_finder(self, myPage):
        myMatch = re.search(r'<h1.*?>(.*?)</h1>', myPage, re.S)
        title = u'暂无标题'
        if myMatch:
            title = myMatch.group(1)
        else:
            print u'爬虫报告：无法加载文章标题'
        title = title.replace('\\','').replace('/','').replace(':','').replace('*','').replace('?','').replace('"', '').replace('>','').replace('<','').replace('|','')
        return title


    def save_data(self, url, title, endPage):
        self.get_data(url, endPage)
        f = open(title+'.txt', 'w+')
        f.writelines(self.datas)
        f.close()
        print u"报告：文件已经下载到本地并打包成txt文件"
        print u'请按任意键退出'
        raw_input()

    def get_data(self, url, endPage):
        url = url + "&pn="
        for i in range(1, endPage+1):
            print u'报告:爬虫%d号正在加载中' %i
            myPage = urllib2.urlopen(url+str(i)).read()
            self.deal_data(myPage.decode('gbk'))

    def deal_data(self, myPage):
        myItems = re.findall('id="post_content.*?>(.*?)</div>', myPage, re.S)
        for item in myItems:
            data = self.mytool.repalce_char(item.replace("\n", "").encode('gbk'))
            self.datas.append(data + '\n')

print u'请输入贴吧地址的最后的字符串：'
bdurl = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))

mySpider = Baidu_Spider(bdurl)
mySpider.baidu_tieba()

