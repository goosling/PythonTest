__author__ = 'joe'
# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like
    # name = Field()
    pass

class zhihuItem(Item):
    title = Field()
    link = Field()
    desc = Field()
