__author__ = 'joe'
#encoding:utf-8

import math
a = float(raw_input('a:'))
b = float(raw_input('b:'))
c = float(raw_input('c:'))
if a != 0:
    delta = b * b - 4 * a * c
    if delta < 0:
        print 'no suolution'
    elif delta == 0:
        s = -b/(2 * a)
        print 's',s
    else:
        root = math.sqrt(delta)
        s1 = (-b+root)/(2*a)
        s2 = (-b-root)/(2*a)
        print 'two distinct solustion are:',s1,s