# Stack is a linear data structure that follows the LIFO (Last In First Out) principle.
# It is a collection of elements that are stored in a linear order and can be accessed in a sequential manner.
# The main operations on a stack are push and pop.
# Push adds an element to the top of the stack, and pop removes the top element from the stack.
# Stack can be implemented using an array or a linked list.

# The operations on a stack are:
# 1. Push: Adds an element to the top of the stack.
# 2. Pop: Removes the top element from the stack.
# 3. Peek: Returns the top element of the stack.
# 4. isEmpty: Returns true if the stack is empty, otherwise false.
# 5. size: Returns the number of elements in the stack.

# Below is an implementation of a stack using an array.

from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def isEmpty(self) -> bool:
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    



