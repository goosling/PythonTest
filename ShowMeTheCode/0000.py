__author__ = 'joe'
# -*- coding: utf-8 -*-

# from PIL import Image, ImageDraw, ImageFont, ImageFilter

# image = Image.open('study.jpg')
# w, h = image.size
# 缩放到50%
# image.thumbnail((w//2, h//2))
# image2 = image.filter(ImageFilter.BLUR)
# image2.save('study.jpg', 'jpeg')
from datetime import date
birthday = date(1991, 9, 20)
now = date.today()
age = now - birthday
print age.days


