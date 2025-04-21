"""
# Problem 1
# Append to Dynamic Array in the end
# Solution: Check if the capacity is equal to the size, double the capacity
# Append the element to the end of the array
# Increment the size
"""

class DynamicArray:
    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def append(self, n):
        if self.capacity == self.length:
            self.resize()

        self.arr[self.length] = n
        self.length += 1
    
    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


# Problem 2
# Insert at a Specified Index
# Shift elements to the right to make space for new element
# Start iterating at the last element adn stop iterating at previous given index
# Insert new element at the given index

    
    def insertIth(self, n, index ):
        if self.length == self.capacity:
            self.resize()
        for index in range(self.length - 1, index - 1, -1):
            self.arr[index + 1] = self.arr[index]
        self.arr[index] = n
        self.length += 1

    

# Problem 3
# Remove an element at a given index from array
# Start iterating at the index after the given index
# Shift it to the left and reduce the length by 1
# Denote the last element as 0

    def removeIth(self, index):
        if self.length == 0:
            print("Error ... Array is empty")
            return
        for index in range(index + 1, self.length):
            self.arr[index - 1] = self.arr[index]
        self.length -= 1
        self.arr[self.length] = 0

        if self.length / self.capacity < .25:
            self.shrink()

# Problem 4
# Shrink when usage is Low. If it drops below 25% of capacity after deletion, shrink to half size
# Check to see if the capacity is equal to the number of elements in the array
# After deletion, compute to get the quotient of length and capacity = (length/capacity)
# If it's below 25%, divide capacity by 2

    def shrink(self):
        if self.length / self.capacity < .25:
            self.capacity = self.capacity // 2
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.arr[i]
        self.arr = new_array

# Problem 5
# Search for a value
# Return the index of the first occurrence of a value in the array
# Loop over the array. Check to see if the value is equal to the search target
# If it is, return the given index. If not, return False

    def searchOccurrence(self, target):
        if self.length == 0:
            print("Error ... Array is empty")
            return
        for i in range(self.length):
            if self.arr[i] == target:
                return i
        return False
                
    

array = DynamicArray(3)

array.append(1)
array.append(2)
array.append(3)
print(array.searchOccurrence(4))
print(array.arr)