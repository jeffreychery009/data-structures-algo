class DoublyNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self, val):
        newNode = DoublyNode(val)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertTail(self, val):
        newNode = DoublyNode(val)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def getLength(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count


    def insertAt(self, val, index):
        if index < 0 or index > self.getLength():
            return
        if index == 0:
            self.insertHead(val)
            return
        if index == self.getLength():
            self.insertTail(val)
            return
        newNode = DoublyNode(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        newNode.next = curr.next
        newNode.prev = curr
        curr.next.prev = newNode
        curr.next = newNode

   
    def deleteHead(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None