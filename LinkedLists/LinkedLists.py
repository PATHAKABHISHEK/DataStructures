################################## Linked List ###############################


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def addNode(self, node):
        currentPointer = self.head
        while not currentPointer.next == None:
            currentPointer = currentPointer.next
        
        currentPointer.next = node
    
    def addNodeAtFirstPosition(self, node):
        node.next = self.head
        self.head = node
    
    def addNodeAtMiddleOfList(self, node, data):
        currentPointer = self.head
        while not currentPointer.data == data:
            currentPointer = currentPointer.next
        
        node.next = currentPointer.next
        currentPointer.next = node
    
    
    def deleteNode(self):
        currentPointer = self.head
        while not currentPointer.next.next == None:
            currentPointer = currentPointer.next
        
        currentPointer.next = None
    
    def deleteFirstNode(self):
        currentPointer = self.head
        self.head = currentPointer.next
    
    def deleteNodeFromMiddleOfList(self, data):
        currentPointer = self.head
        while not currentPointer.next.data == data:
            currentPointer = currentPointer.next

        currentPointer.next = currentPointer.next.next

    
    def printLinkedList(self):
        currentPointer = self.head
        while not currentPointer.next == None:
            print(currentPointer.data, end=' ')
            currentPointer = currentPointer.next
        
        print(currentPointer.data, end=' ')
        
        
head = Node(5)
myLinkedList = LinkedList(head)
myLinkedList.addNode(Node(11))
myLinkedList.addNode(Node(500))
myLinkedList.addNode(Node(12))
myLinkedList.addNode(Node(99))
myLinkedList.addNodeAtFirstPosition(Node(43))
myLinkedList.addNodeAtMiddleOfList(Node(89), 500)
myLinkedList.deleteFirstNode()
myLinkedList.deleteNodeFromMiddleOfList(89)
myLinkedList.deleteNode()
myLinkedList.printLinkedList()
        





