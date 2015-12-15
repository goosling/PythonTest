__author__ = 'joe'
# -*- coding: utf-8 -*-

from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 要提取的网页url
url = 'http://www.zhihu.com/question/30408972'

def extract(url):
    g = Goose({'stopwords_class': StopWordsChinese})
    article = g.extract(url=url)
    return article.cleaned_text

if __name__ == "__main__":
    print extract(url)

