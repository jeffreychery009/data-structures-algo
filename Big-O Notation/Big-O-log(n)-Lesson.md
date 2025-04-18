# O(log n) - Logarithmic Time Complexity

O(log n) represents logarithmic time complexity, where the runtime grows logarithmically with the input size. This is one of the most efficient time complexities after O(1), as the time taken grows very slowly as the input size increases.

## Characteristics
- Runtime grows logarithmically with input size
- Very efficient for large datasets
- Usually involves dividing the problem size by a constant in each step
- Common in algorithms that divide and conquer
- Often seen in binary operations and tree structures

## How to Spot O(log n):
1. Division of Problem Space:
   ```python
   while n > 1:
       n = n // 2  # Dividing the problem size by 2 in each iteration
   ```

2. Binary Search Pattern:
   ```python
   left, right = 0, len(arr) - 1
   while left <= right:
       mid = (left + right) // 2
       if arr[mid] == target:
           return mid
       elif arr[mid] < target:
           left = mid + 1
       else:
           right = mid - 1
   ```

3. Tree Traversal Patterns:
   ```python
   def binary_tree_height(node):
       if not node:
           return 0
       return 1 + max(binary_tree_height(node.left), 
                     binary_tree_height(node.right))
   ```

## Common O(log n) Algorithms:

### 1. Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found
```

### 2. Finding Power of Two
```python
def is_power_of_two(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True
```

### 3. Binary Tree Operations
```python
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root
```

## Visual Representation
```
Time │
     │    ┌─── O(log n)
     │   ╱
     │  ╱
     │ ╱
     │╱
     └──────────────
       Input Size (n)
```

## When to Use O(log n) Algorithms:
1. Searching in sorted arrays
2. Binary tree operations
3. Number manipulation involving powers
4. When efficiency is crucial for large datasets

## Common Use Cases:
1. Search Operations
   - Binary search in sorted arrays
   - Binary search trees
   - Finding elements in balanced trees

2. Mathematical Operations
   - Computing powers
   - Finding square roots
   - Base conversion

3. Data Structure Operations
   - Balanced BST operations
   - Heap operations
   - Skip lists

## Performance Comparison
```
Input Size (n) | Operations (log n)
--------------|------------------
10            | 3.32
100           | 6.64
1,000         | 9.97
1,000,000     | 19.93
1,000,000,000 | 29.90
```

## Space Complexity
Most O(log n) algorithms have O(1) space complexity when implemented iteratively, but might have O(log n) space when implemented recursively due to the call stack.

## Optimization Tips:
1. Use iterative implementation when possible to save space
2. Ensure data is sorted for binary search
3. Keep binary trees balanced
4. Consider using binary search variants:
   ```python
   def exponential_search(arr, target):
       if arr[0] == target:
           return 0
       
       i = 1
       while i < len(arr) and arr[i] <= target:
           i = i * 2
       
       return binary_search(arr, target, i//2, min(i, len(arr)-1))
   ```

## Real-World Analogies:
Think of O(log n) like:
- Finding a word in a dictionary (dividing pages in half each time)
- Guessing a number between 1-100 (binary search strategy)
- Looking for a book in a library using the Dewey Decimal System

## Why O(log n) is Efficient:
- For a problem size of 1 million, only about 20 steps needed
- Doubling the input size only adds one extra step
- Extremely scalable for large datasets

## Common Mistakes to Avoid:
1. Assuming array is sorted for binary search
2. Not handling edge cases (empty arrays, single elements)
3. Integer overflow in mid-point calculation
4. Unbalanced binary trees degrading to O(n)

Remember: O(log n) algorithms are extremely efficient and should be used whenever possible, especially when dealing with large datasets. They're often the optimal solution for search-based problems with sorted data.
