__author__ = 'joe'
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
import requests

file_name = 'filtered_words.txt'
file_content = ''
file_content += '生成时间'+time.asctime()

url = 'http://www.zhihu.com/question/30408972'

def zhihu_spider(url):
    global file_content
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text)

    title_divide = '\n'+'--'*30+'\n'+'\n'+'--'*30+'\n'
    file_content += title_divide + '\t'*4 + '内容' + ':'+title_divide
    count = 1
    # 得到内容的soup对象
    list_soup = soup.find('div', {'class': 'class="zm-item-rich-text'})
    for info in list_soup:
        content = info.find('div', {'class': ' zm-editable-content clearfix'}).string.strip()
        file_content += content

def do_spider(url):
    zhihu_spider(url)

f = open(file_name, 'w')
f.write(file_content)
f.close()
