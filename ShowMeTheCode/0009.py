__author__ = 'joe'
# -*- coding: utf-8 -*-

import re
import urllib2

def file_read(filename):
    req = urllib2.Request('http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html')
    r = urllib2.urlopen(req)
    html = r.read()
    return html

def link_find(html):
    match = re.findall(r'href="(http[s]?:[^"]+)"', html)
    return match

def main():
    html = file.read('http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html')
    link = link_find(html)
    for string in link:
        print string

if __name__ == '__main__':
    main()