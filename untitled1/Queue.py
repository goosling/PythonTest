__author__ = 'joe'

class Queue(object):
    def __init__(self, queue):
        self.queue = queue
    def enqueue(self, element):
        # append the element
        self.queue.append(element)
    def dequeue(self):
        # delete the first num in queue
        element = self.queue[0]
        self.queue = self.queue[1:]
        return element
    # need this part ,you should find out why
    def __str__(self):
        return str(self.queue)
    __repr__ = __str__
queue = Queue([1, 2, 3, 4])
print queue
queue.enqueue(5)
queue.dequeue()
print queue