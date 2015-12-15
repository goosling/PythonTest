__author__ = 'joe'
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
    fillColor = '#ff0000'
    width, height = img.size
    draw.text((width-40, 0), '99', font=font, fill=fillColor)
    img.save('add_num.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    image = Image.open('study.jpg')
    add_num(image)