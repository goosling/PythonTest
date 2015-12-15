__author__ = 'joe'
# !/usr/bin/env python

import threading
from time import ctime, sleep
from random import randint
from Queue import Queue


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super(MyThread, self).__init__()
        self.func = func
        self.name = name
        self.args = args
    def run(self):
        print 'starting', self.name, 'at:', ctime()
        self.res = self.func(*self.args)
        print self.name, 'finished at:', ctime()
    def getResult(self):
        return self.res

def writeQ(queue):
    print 'producing object for Q....'
    queue.put('xxxx', 1)
    print 'size now', queue.size()
def readQ(queue):
    val = queue.get(1)
    print 'consumed object from Q...size now', queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))
def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))
funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads.start()
    for i in nfuncs:
        threads.join()
    print 'all done'
if __name__ == '__main__':
    main()