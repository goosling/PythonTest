__author__ = 'joe'
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

def run_proc(name):
    print 'run child process %s (%s)....' % (name, os.getpid())

if __name__ == 'main':
    print 'Parent process %s.' % os.getpgid()
    p = Process(target=run_proc, args=('test',))
    print 'process will start...'
    p.start()
    p.join()
    print 'process end'