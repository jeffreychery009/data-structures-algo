
# Linked List are a linear data structure that store elements in a sequential manner.
# Each element in a linked list is called a node, and each node contains a value and a pointer to the next node.
# The first node is called the head, and the last node is called the tail.
# The tail node points to None, indicating the end of the list.

# Linked List are dynamic, meaning they can grow and shrink as needed.
# They are also non-contiguous, meaning the elements are not stored in a contiguous block of memory.
# This allows for more efficient memory usage.

# Linked List are also called a singly linked list, because each node points to the next node.

# Below is how you implement a linked list:
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertHead(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
    
    def insertTail(self, val):
        if self.head is None:
            self.insertHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
    
    def deleteHead(self):
        if self.head is None:
            return None
        self.head = self.head.next
    
    def deleteEnd(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
    
    def printList(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
    

# Below are additional methods that can be added to a linked list:

    def search(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False
    
    def getLength(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        

    def insertAt(self, val, index):
        if index < 0 or index > self.getLength():
            return
        if index == 0:
            self.insertHead(val)
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        newNode = ListNode(val)
        newNode.next = curr.next
        curr.next = newNode
        
    def deleteAt(self, index):
        if index < 0 or index >= self.getLength():
            return
        if index == 0:
            self.deleteHead()
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next