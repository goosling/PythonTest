__author__ = 'joe'
# -*- coding: utf-8 -*-

import string, random


# 激活码中的数字和字母符号等
pool = string.ascii_letters + string.digits
# 获得四个字母和数字的随机组合
def getRandom():
    return ''.join(random.sample(pool, 4))

# 生成激活码的组数
def getCodeNum(group):
    return '-'.join([getRandom() for i in range(group)])

# 生成n组激活码
def generate(n):
    return [getCodeNum(4) for i in range(n)]

if __name__ == '__main__':
    for i in range(20):
        print generate(1)
