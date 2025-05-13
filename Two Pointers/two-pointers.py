# Two Pointers
# Two Pointers is a technique used to solve problems by using two pointers to traverse the array or string.

# We initialize two pointers, one at the beginning and one at the end of the array or string.
# We then move the pointers towards each other until they meet.
# We can use this technique to solve problems like finding the sum of two numbers in an array, finding the largest sum of a subarray, etc.

# Here is how to initialize the pointers:
# left = 0 , right = len(array) - 1 -> which indicates the last index of the array

# We move the pointers towards each other to satisfy a given condition.



# Check if a string is a Palindrome
# A palindrome is a set of words that written backwards, spells the exact same thing.
# Example words: Eve, level, civic, madam... etc.

def isPalindrome(word):
    # Initialize two pointers
    L, R = 0, len(word) - 1

    # We move the pointers until R is not greater than L
    # Check if each letter are the same. If not, return False
    # Keep incrementing and decrementing to satisfy the condition

    while L < R:
        if word[L] != word[R]: 
            return False
        L += 1
        R -= 1
    return True

# Test example
print(isPalindrome('eve')) # Expected Output: True
print(isPalindrome('classic')) # Expected Output: False


# Problem Set 2
# Target Sum
# We're working with an array that is sorted in non-decreasing order.
# Iterate through the array to find the indices that match to the target sum.

def targetSum(array, target):
    # Initialize two pointers
    L, R = 0, len(array) - 1

    while L < R:
        if array[L] + array[R] > target:
            R -= 1
        elif array[L] + array[R] < target:
            L += 1
        else:
            return [L, R]
    

# Test Example
arr = [-1, 0, 2, 3, 5, 8, 7, 10]
result = targetSum(arr, 8) # Expected Output: [3, 4]
print(f"Answer is:  {result}")