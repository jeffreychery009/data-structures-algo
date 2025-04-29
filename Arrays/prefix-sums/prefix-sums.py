# Prefix Sum
# Prefix sum is a very important concept in array problems.
# It can be used to calculate the sum of a subarray in O(1) time.
# How to define a prefix sum array?

# First we need to define a prefix sum array.
# The prefix sum array is a new array that stores the sum of all the elements from the start to the current index.
# For example, if we have an array [1, 2, 3, 4, 5], the prefix sum array is [1, 3, 6, 10, 15].

# How to use the prefix sum array to calculate the sum of a subarray?

# For example, if we have an array [1, 2, 3, 4, 5], and we want to calculate the sum of the subarray from index 1 to index 3, we can use the prefix sum array to do this.
# The sum of the subarray from index 1 to index 3 is 2 + 3 + 4 = 9.
# We can use the prefix sum array to calculate this by using the formula:
# sum = prefix[right] - prefix[left - 1]
# where left is the start index of the subarray and right is the end index of the subarray.

# In our case, left = 1 and right = 3.
# So, sum = prefix[3] - prefix[1 - 1] = 15 - 1 = 14.

# This is the sum of the subarray from index 1 to index 3.

# Now, let's implement the prefix sum array in Python.

class PrefixSum:
    def __init__(self, nums):
        self.prefix = [] # Initialize the prefix sum array
        total = 0 # Initialize the total sum
        for n in nums: # Iterate through the array
            total += n # Add the current element to the total
            self.prefix.append(total)

    def range_sum(self, left, right):
        preRight = self.prefix[right] # Get the prefix sum of the right index
        preleft = self.prefix[left - 1] if left > 0 else 0 # Get the prefix sum of the left index
        return preRight - preleft # Return the difference between the prefix sum of the right and left indices
    
# Example usage
nums = [1, 2, 3, 4, 5]
prefixSum = PrefixSum(nums)
print(prefixSum.range_sum(1, 3)) # Output: 9


