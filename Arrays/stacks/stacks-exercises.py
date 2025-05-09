# Problem 1
# Reverse a String

def reverseString(s):
    stack = []
    for char in s:
        stack.append(char)
    reverse_str = ''
    while stack:
        reverse_str += stack.pop()
    return reverse_str

print(reverseString('hello')) # Simulating the answer

# Problem 2
# Reverse a List
# Given a list, return a new list that is the reverse of the original list
def reverseList(lst):
    stack = []
    for num in lst:
        stack.append(num)
    reverse_stk = []
    while stack:
        reverse_stk.append(stack.pop())
    return reverse_stk

num = [1, 2, 3, 4]
print(reverseList(num)) # Simulating the answer

# Problem 3
# Print stack from top to bottom
def printStack(lst):
    while lst:
        print(lst.pop())



# Problem 4
# Check if the given word is a palindrome
def isPalindrome(word):
    stack = []
    for char in word:
        stack.append(char)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str == word

print(isPalindrome('eve'))

# Problem 5
# Given a stack, return the top item without removing it
def findTopItem(lst):
    if not lst:
        return None
    return lst[-1]

num1 = [1, 2, 3, 4, 5, 6]
print(findTopItem(num1))

# Problem 6
# Count the items in a stack
def countStack(lst):
    count = 0
    for num in lst:
        count += 1
    return count

num2 = [1, 2, 3, 4, 5, 6, 7, 10]
print(countStack(num2))


# Problem 7
# Undo an action problem
def undo(actions):
    stack = []
    for action in actions:
        if action != 'UNDO':
            stack.append(action)
        elif stack:
            stack.pop()
    return stack


def validParentheses(s):
    stack = []
    mapping = {')' : '(', ']' : '[', '}' : '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        if char in ')]}':
            if len(stack) == 0:
                return False
            top = stack.pop()
            if mapping[char] != top:
                return False
    return len(stack) == 0