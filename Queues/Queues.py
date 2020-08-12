##################################### Queue ###################################

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.insert(0, element)
    
    def dequeue(self):
        if not len(self.queue) == 0:
            self.queue.pop()
        else:
            print("Queue is Empty, Can't Pop")
    
    def getSizeOfQueue(self):
        return len(self.queue)
    
    def getElementsOfQueue(self):
        return self.queue

myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue(1)
myQueue.enqueue(0)
myQueue.enqueue(12)
myQueue.enqueue(14)

print(myQueue.getElementsOfQueue())
myQueue.dequeue()
print(myQueue.getElementsOfQueue())
myQueue.dequeue()
print(myQueue.getElementsOfQueue())
myQueue.dequeue()
print(myQueue.getElementsOfQueue())
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.getElementsOfQueue())
myQueue.dequeue()