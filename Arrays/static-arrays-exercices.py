"""
# Problem 1
# find the maximum number in the array
# Solution: Iterate over all the elements
# Store the first element as the max element
# Compare each element with the max
# Return the max
"""
array = [3, 7, 1, 9, 2]
def findMax(arr, length):
    max_value = arr[0]
    for index in range(length):
        if arr[index] > max_value:
            max_value = arr[index]
    return max_value

print(f"\nOriginal Array: {array}")
max = findMax(array, len(array))
print(f"Max value: {max}")

"""
# Problem 2
# find count occurrences of a number
# Solution: Define a count variable
# Iterate over the array. If the target is there, increment count
# Return count
"""
array1 = [3, 5, 3, 10, 5, 3, 5]
def countOccurences(arr, target, length):
    if length == 0:
        return None
    count = 0
    for index in range(length):
        if arr[index] == target:
            count += 1
    return count

print(f"\nOriginal Array: {array1}") # Output: [3, 5, 3, 10, 5, 3, 5]
occurences = countOccurences(array1, 3, len(array1))
print(f"Occurences of 3: {occurences}") #Output: 3
        

"""
# Problem 3
# Return a new array that is reverse of the original
# Solution: Define a temp array with the same size as the original array
# Loop over the elements of the original in reverse
# Copy each element in the original array
# Return the original aray
"""
array2 = [1, 2, 3, 4, 5]
def reverseArray(arr, length):
    n = length

    temp = [0] * n

    for i in range(n):
        temp[i] = arr[n - i - 1]

    for i in range(n):
        arr[i] = temp[i]
    
    return arr

print(f"\nOriginal Array: {array2}")
new_array = reverseArray(array2, len(array2))
print(f"Reverse Array: {new_array}")


"""
# Problem 4
# Return true if the array is sorted in ascending order, else false
# Solution: Start looping at the first index or second position
# Compare if the element at said index is less than the element previous to it.
# If less, return False. Otherwise return True
"""

array3 = [1, 2, 3, 5, 9]
def isSorted(arr, length):
    
    for index in range(1, length):
        if arr[index] < arr[index - 1]:
            return False        
    return True
        
print(f"\nOriginal Array: {array3}")
sorted = isSorted(array3, len(array3))
print(f"Is it sorted: {sorted}")

"""
# Problem 5
# Return the sum of all even numbers
# Solution: Define a variable total to keep count of the total
# Loop over the array. Check if the element have a modulo of 0 (means they're even)
# If they are even, add them to the total variable
# Return the total
"""

array4 = [1, 2, 3, 4, 7, 8, 10]
def sumOfEvenNumbers(arr, length):
    total = 0

    for index in range(length):
        if arr[index] % 2 == 0:
            total += arr[index]
    
    return total

print(f"\nOriginal Array: {array4}")
even_total = sumOfEvenNumbers(array4, len(array4))
print(f"Even Numbers Total: {even_total}")