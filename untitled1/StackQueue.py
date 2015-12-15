__author__ = 'joe'

class StackQueue(object):
    def __init__(self, stackqueue):
        self.stackqueue = stackqueue
    def isEmpty(self):
        return (not len(self.stackqueue))
    def shift(self):
        if self.isEmpty():
            print "Empty, can not shift"
        else:
            element = self.stackqueue[0]
            self.stackqueue = self.stackqueue[1:]
            return element

    def unshift(self, element):
        self.stackqueue = [element]+self.stackqueue

    def push(self, element):
        self.stackqueue.append(element)

    def pop(self):
        self.stackqueue.pop()

    def __str__(self):
        return str(self.stackqueue)
    __repr__ = __str__

stkq = StackQueue([1, 2, 3])
print stkq
print stkq.shift()
stkq.unshift(6)
print stkq
stkq.push(7)
print stkq
stkq.pop()
print stkq
