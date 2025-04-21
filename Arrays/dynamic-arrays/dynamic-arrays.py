# Dynamic Arrays

# Dynamic arrays are arrays that can grow or shrink in size
# They are implemented using a pointer to the memory address of the array
# The pointer is then moved to a new memory address when the array is resized

# Below is an implementation of a dynamic array in Python and its operations

# Here we defined the Dynamic Array class, setting up the size and the capacity

class DynamicArray:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * capacity

# Function to retrieve the element at a given index.
# Time complexity results in Big O(1)

    def get(self, index, length):
        if index < 0 or index >= length:
            print(f"Error ... {index} out of bounds.")
            return None
        
        return self.arr[index]
    
# Function to add an element at a given index.
# Time complexity results in Big O(1)
    def set(self, index, length, n):
        if index < 0 or index >= length:
            print(f"Error ... {index} out of bounds.")
            return None
        
        self.arr[index] = n

# Function return the size of the array
    def getSize(self) -> None:
        if self.size == 0:
            print("Array is empty")
        return self.size

# Function return the capacity of the array
    def getCapacity(self) -> None:
        return self.capacity
    
# Function to resize the array if it's full
# Time complexity is Big O(n) because we have to copy all the elements of the array into a new array
    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.arr[i]
        self.arr = new_array

# Function to add an element to the end of the array
# Time complexity is Big O(1) because we're just adding an element to the end of the array
    def pushback(self, n) -> None:
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

# Function to remove the last element of the array
# Time complexity is Big O(1) because we're just removing the last element of the array
    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]

# Function to print the array
# Time complexity is Big O(n) because we're just printing the array
    def printArray(self) -> None:
        for i in range(self.size):
            print(self.arr[i], end=" ")
            
array = DynamicArray(3)

array.arr[0] = 1
array.arr[1] = 2
array.arr[2] = 3

print(array.get(4, 3))
