__author__ = 'joe'

import math
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def get_xy(self):
        return (self.__x, self.__y)
    def set_xy(self, point):
        self.__x, self.__y = point
    def __str__(self):
        return "%d:%d" % (self.__x, self.__y)
    __repr__ = __str__
    point = property(get_xy, set_xy)

class Line(object):
    pointStart = Point
    pointEnd = Point
    def __init__(self, pointStart, pointEnd):
        self.pointStart = pointStart
        self.pointEnd = pointEnd
    def get_line(self):
        return (self.pointStart, self.pointEnd)
    def set_line(self, line):
        self.pointStart, self.pointEnd = line
    def __str__(self):
        return "%d---->%d" %(self.pointStart, self.pointEnd)
    def length(self):
        return math.sqrt((self.pointStart.x-self.pointEnd.x)**2+(self.pointStart.y - self.pointEnd.y)**2)
    __repr__ = __str__
    line = property(get_line, set_line)

p1 = Point(2, 3)
p2 = Point(5, 6)
l1 = Line(p1, p2)
print l1.length()


