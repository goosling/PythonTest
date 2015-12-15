__author__ = 'joe'
# !/usr/bin/env python

import threading
from time import ctime, sleep

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super(MyThread, self).__init__()
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print 'starting', self.name, 'at:', ctime()
        self.res = self.func(*self.args)
        print self.name, 'finished at:', ctime()

    def getResult(self):
        return self.res

def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)

def fac(x):
    sleep(0.01)
    if x < 2:
        return 1
    return x * fac(x - 1)

def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum(x - 1)

func = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(func))
    print "***single thread"
    for i in nfuncs:
        print 'starting', func[i].__name__, 'at:', ctime()
        print func[i](n)
        print func[i].__name__, 'finished at:', ctime()
    print '\n***multiple threads'
    threads = []
    for i in nfuncs:
        t = MyThread(func[i], (n,), func[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()
    print 'all done'
if __name__ == '__main__':
    main()