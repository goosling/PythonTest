__author__ = 'joe'
# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import urllib2
# 伪造浏览器标识
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:8.0.1) Gecko/20100101 Firefox/8.0.1'}
num = 1
url = 'http://tieba.baidu.com/p/2166231880'
download_file = 'C:/Users/joe/Desktop/diary'

# 定义一个抓取函数，可以用作图片、内容抓取
def get_page(url):
    urlContent = urllib2.urlopen(url).read()
    return urlContent

content = get_page(url)
soup = BeautifulSoup(content)
# 用bs4解析<cc>标签内的href就是图片文件
