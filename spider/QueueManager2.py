__author__ = 'joe'
# -*- coding: utf-8 -*-

import time, sys, Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，即为运行QueueManager1.py的机器
server_addr = '127.0.0.1'
print('Connect to server %s....' % server_addr)
# 端口和验证码要和QueueManager1保持一致
m = QueueManager(address=(server_addr, 5000), authkey='abc')
# 从网络连接
m.connect()
# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取人物，将其写入result中
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print 'task Queue is Empty'

print 'work exit'