# Static Arrays

# Static arrays are a fixed size, and the size must be known at compile time.
# They are stored in contiguous memory locations.
# They are a type of data structure that stores a fixed number of elements of the same type.

#Initialize an array
array = [1, 2, 3, 4, 0]

#Access an element
print(array[0]) # Output: 1

#Traversing an array
for i in range(len(array)):
    print(array[i])

# Or
i = 0
while i < len(array):
    print(array[i])
    i += 1

# Deleting the element at the last position
def removeEnd(arr, length):
    if length > 0:

        # Denote the last element/ replacing with 0
        arr[length - 1] = 0

def removeIthIndex(arr, i, length):
    # Check if index is valid
    if i < 0 or i >= length:
        return length
        
    # Shift elements to the left
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # Set the last element to 0
    arr[length - 1] = 0
    # Return new length
    return length - 1


# Inserting an element at the end
def insertEnd(arr, length, n):
    if arr[length - 1] == 0:
        arr[length - 1] = n
    return length + 1



def insertIth(arr, length, n, i):
    # Check if array is full
    if length >= len(arr):
        return length
    
    # Check if index is valid
    if i < 0 or i > length:
        return length
        
    # Shift elements to the right, starting from the end
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
        
    # Insert the new element
    arr[i] = n
    
    # Return new length
    return length + 1

# Test the function
# Example usage:
array = [1, 2, 3, 4, 0]  # Array with capacity 5, logical length 4
print("Original array:", array)
new_length = insertIth(array, 4, 9, 0)  # Insert 9 at index 0
print("After insertion:", array)
print("New length:", new_length)
