__author__ = 'joe'
# !/usr/bin/env python

from time import ctime, sleep

def loop0():
    print 'start loop0 at:', ctime()
    sleep(4)
    print 'loop0 done at:', ctime()
def loop1():
    print 'start loop1 at:', ctime()
    sleep(2)
    print 'loop1 done at:', ctime()

def main():
    print 'starting at:', ctime()
    loop0()
    loop1()
    print 'all done at:', ctime()

if __name__ == '__main__':
    main()