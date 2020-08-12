##################################### Stacks #################################

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if not len(self.stack) == 0:
            self.stack.pop()
        else:
            print("Stack is Empty, Can't Pop")   
        
    def getTopElementOfStack(self):
        if not len(self.stack) == 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
   
    def getElementsOfStack(self):
        return self.stack
    
    def sizeOfStack(self):
        return len(self.stack)


myStack = Stack()
myStack.push(5)
myStack.push(6)
myStack.push(12)
myStack.push(16)

# print(myStack.getTopElementOfStack())

print(myStack.getElementsOfStack())
myStack.pop()
print(myStack.getElementsOfStack())
myStack.pop()
print(myStack.getElementsOfStack())
myStack.pop()
print(myStack.getElementsOfStack())
myStack.pop()
print(myStack.getElementsOfStack())
myStack.pop()
# print(myStack.sizeOfStack())
