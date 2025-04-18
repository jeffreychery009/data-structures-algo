# O(n²) - Quadratic Time Complexity

O(n²) represents quadratic time complexity, where the runtime grows proportionally to the square of the input size. This means that as the input size grows, the runtime grows much more rapidly than linear time complexity.

## Characteristics
- Runtime grows quadratically with input size
- If input size doubles, runtime increases four-fold
- Usually involves nested iterations over the data
- Common in algorithms with nested loops
- Generally try to avoid when possible for large datasets

## How to Spot O(n²):
1. Nested Loops:
   ```python
   for i in range(n):
       for j in range(n):
           # do something
   ```

2. Triangular Patterns:
   ```python
   for i in range(n):
       for j in range(i):
           # do something
   ```

3. Multiple Iterations Over Same Data:
   ```python
   for i in range(n):
       for j in range(n):
           if arr[i] < arr[j]:
               # do something
   ```

## Common O(n²) Algorithms:

### 1. Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### 2. Selection Sort
```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 3. Matrix Operations
```python
def print_all_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(f"({arr[i]}, {arr[j]})")
```

## Visual Representation
```
Time │       ╱
     │      ╱
     │     ╱
     │    ╱
     │   ╱
     │  ╱ O(n²)
     │ ╱
     │╱
     └──────────────
       Input Size (n)
```

## When to Use O(n²) Algorithms:
1. Small input sizes where simplicity is more important than efficiency
2. Educational purposes (learning basic sorting algorithms)
3. When working with small matrices or 2D arrays
4. When the overhead of more efficient algorithms isn't worth it for small n

## When to Avoid O(n²):
1. Large datasets (n > 10,000)
2. Performance-critical applications
3. Real-time systems
4. Mobile applications where battery life is important

## Common Use Cases:
1. Simple sorting algorithms
   - Bubble Sort
   - Selection Sort
   - Insertion Sort

2. Matrix/2D Array Operations
   - Matrix multiplication
   - Finding all possible pairs
   - Grid traversal

3. Comparison-based operations
   - Finding all duplicates
   - Comparing all elements with each other

## Space Complexity
Most O(n²) algorithms have O(1) space complexity as they often sort or process in place, but some might require O(n²) space:
- Creating a new n×n matrix
- Storing all possible pairs of elements

## Optimization Tips:
1. Consider using more efficient algorithms for large datasets:
   - Replace bubble sort with quicksort O(n log n)
   - Use hash tables to avoid nested loops O(n)
   
2. Early termination when possible:
   ```python
   def has_duplicate(arr):
       for i in range(len(arr)):
           for j in range(i + 1, len(arr)):  # Note: j starts from i + 1
               if arr[i] == arr[j]:
                   return True  # Exit early when found
       return False
   ```

## Real-World Analogies:
Think of O(n²) like:
- Comparing every person in a room with every other person
- Checking every cell in a spreadsheet against every other cell
- Finding all possible combinations of items in two lists

## Performance Impact Example:
```
Input Size (n) | Operations (n²)
--------------|-----------------
10            | 100
100           | 10,000
1,000         | 1,000,000
10,000        | 100,000,000
```

Remember: While O(n²) algorithms are not always optimal for large datasets, they can be perfectly acceptable or even preferred for small inputs due to their simplicity and low overhead.
