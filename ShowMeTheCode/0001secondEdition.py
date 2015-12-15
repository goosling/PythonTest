__author__ = 'joe'
# -*- coding: utf-8 -*-

import string, random

class LengthError(ValueError):
    def __init__(self, arg):
        self.args = arg

def pad_zero_to_left(inputNumString, totalLength):
    lengthOfInput = len(inputNumString)
    if lengthOfInput > totalLength:
        raise LengthError('Error')
    else:
        return '0'*(totalLength - lengthOfInput) + inputNumString

poolOfChars = string.ascii_letters + string.digits
randomCodes = lambda x, y: ''.join([random.choice(x) for i in range(y)])

def invitation_code_generator(num, lengthOfRandom, lengthOfKey):
    notice = 'L'
    for i in range(num):
        tempString = ''
        try:
            yield randomCodes(poolOfChars, lengthOfRandom) + notice+\
                pad_zero_to_left(str(i), lengthOfKey)
        except LengthError:
            print 'Error'
for code in invitation_code_generator(200, 16, 4):
    print code

