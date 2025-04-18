# What is Big-O Notation?

It's basically a way to analyze the run time of our algorithm to execute as the input size of our
algorithm grow. 

# O(1) - Constant Time Complexity

O(1) represents constant time complexity. This means that regardless of the input size (n), the algorithm will always perform the same number of operations.

## Characteristics
- Execution time stays the same regardless of input size
- Considered the most efficient Big O time complexity
- No loops or recursion involved
- Direct operations only

## Examples of O(1) Operations:
1. Array operations:
   - Accessing an element by index: `array[5]`
   - Setting a value at a known index: `array[5] = 10`
   - Adding/removing at the beginning/end of an array (when using appropriate data structures)

2. Hash table/dictionary operations:
   - Inserting a key-value pair
   - Looking up a value by key
   - Deleting a key-value pair

3. Mathematical operations:
   - Basic arithmetic (+, -, *, /)
   - Comparison operations (<, >, ==)
   - Variable assignment

## Visual Representation
```
Time │    O(1)
     │─────────────
     │
     │
     └──────────────
       Input Size (n)
```

## Code Example
```python
def get_first_element(array):
    return array[0]  # O(1) - always returns first element instantly

def check_if_even(number):
    return number % 2 == 0  # O(1) - single operation regardless of number size
```

## Why It's Important
Understanding O(1) operations is crucial because:
- They are the building blocks of more complex algorithms
- They represent the ideal performance scenario
- They help in optimizing critical parts of your code where performance matters

Remember: While O(1) operations are very fast, they might not always be the best choice when considering other factors like code readability or maintenance.

