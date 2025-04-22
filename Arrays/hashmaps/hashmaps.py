# Hashmaps are a data structure that store key-value pairs
# They are also known as dictionaries in Python
# They are used to store data in a way that allows for fast retrieval of data, insertion, deletion, and update of data


# Hashmaps are implemented using arrays
# Basic operations results in Big O(1) time complexity

# Under the hood, hashmaps use a hash function to hash the key and store the value at the index of the hash
# The hash function takes the key and returns an index in the array
# The hash function should be a one-to-one function, meaning that each key maps to exactly one index

# By using the key, we can retrieve the value from the array in constant time. Same goes for insertion, deletion, and update
# It's possible that two keys can hash to the same index, this is known as a collision
# Collisions are handled using a technique called chaining and the array will store a linked list at each index
# Traversing the list will result in a time complexity of Big O(n)

# Another technique to handle collisions is open addressing
# Open addressing is a technique where we store the value at the next available index in the array
# If the index is already occupied, we will search for the next available index and store the value there
# This technique is known as linear probing

# Below we will implement a hashmap under the hood using an array.


class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
class HashMap:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.map = [None, None]


    # Hash function to hash the key and return an index
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
    
    # Get the value of the key
    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None
    
    # Remove the key
    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity
        
    
    # Insert the key and value
    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
            index += 1
            index = index % self.capacity
        
    # Rehash the map
    def rehash(self):
        self.capacity = self.capacity * 2
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)


    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)







