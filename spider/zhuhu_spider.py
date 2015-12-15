__author__ = 'joe'
# -*- coding: utf-8 -*-

from scrapy.spider import Spider

class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'http://www.zhihu.com/'
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2]
        open(filename, 'wb').write(response.body)
