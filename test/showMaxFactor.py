__author__ = 'joe'

def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print 'largest num of %d is %d'% (num,count)
            break

        else:
            print num, 'is prime'
        count -= 1


for eachNum in range(10, 22):
    showMaxFactor(eachNum)