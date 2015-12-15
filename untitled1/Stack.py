__author__ = 'joe'

class Stack(list):
    def __init__(self, stack):
        super(Stack, self).__init__()
        self.stack = stack
    # 在尾部压入一个新元素
    def push(self, oneElement):
        self.stack.append(oneElement)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return (not len(self.stack))
    def peek(self):
        return self.stack[-1]
    def __str__(self):
        return str(self.stack)
    __repr__ = __str__

stk = Stack([1, 2, 3])
stk.push(4)
print stk
print stk.pop()
print stk.isEmpty()