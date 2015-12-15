__author__ = 'joe'
# -*- coding: utf-8 -*-
import os
from PIL import Image

class change_DPI:
    def __init__(self):
        self.path = None

    def setPath(self, path):
        self.path = path

    def change_DPI(self):
        files = os.listdir(self.path)
        isExist = False
        for f in files:
            if f.endswith(('jpg', 'png')):
                isExist = True
                path_name = os.path.join(self.path, f)
                # print path_name
                image = Image.open(path_name)
                x_iP5 = 1136
                y_iP5 = 640
                (x, y) = image.size
                print ('origin image size is: ', image.size)
                if x > x_iP5 or y > y_iP5:
                    if x > x_iP5:
                        x_resize = x_iP5
                        y_resize = int(y*(x_resize/x))
                        f_resize = image.resize((x_resize, y_resize))
                        f_resize.save(f)
                        continue
                    if y > y_iP5:
                        y_resize = y_iP5
                        x_resize = int(x*(y_resize/y))
                        f_resize = image.resize((x_resize, y_resize))
                        f_resize.save(f)
                        continue
                '''
                changeX = int(x)/x_iP5
                changeY = int(y)/y_iP5
                # 判断分辨率是否满足
                if changeX > 1 or changeY > 1:
                    change = changeX if changeX > changeY else changeY
                    img = image.resize((int(x/change), int(y/change)))
                    img.save('result.jpg), 'jpeg')
                '''
        if isExist == False:
            print ('no photo')

if __name__ == '__main__':
    test = change_DPI()
    test.setPath('.')
    test.change_DPI()

