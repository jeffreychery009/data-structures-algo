# Problem 1 
# Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e., nums[left] + nums[left + 1] + ... + nums[right]).

class NumArray:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft
    


# Problem 2
# Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
# If no such index exists, return -1.


class Solution:
    def getPivotIndex(self, nums) -> int:

        total = 0
        leftTotal = 0

        for num in nums:
            total += num

        for i in range(len(nums)):
            if leftTotal == total - leftTotal - nums[i]:
                return i
            leftTotal += nums[i]
        return -1
    
# Example usage
nums = [1, 7, 3, 6, 5, 6]
solution = Solution()
print(solution.getPivotIndex(nums)) # Output: 3


# Problem 4
# Subarray Sum Equals k

class Solution:
    def subarray(self, nums, k: int) -> int:
        
        prefix_sum_count = {0:1}
        prefix_sum = 0
        count = 0


        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1
        
        return count

            
# Example usage
nums = [1, 2, 3, 4, 5]
k = 3
solution = Solution()
print(solution.subarray(nums, k)) # Output: 2


# Problem 4
# Left and Right Sum Differences

def leftRightSum(nums):
    res = [0] * (len(nums))

    prefix = 0
    for i in range(len(nums)):
        res[i] = prefix
        prefix += nums[i]

    postfix = 0
    for i in range(len(nums) - 1, -1, -1):
        res[i] = abs(res[i] - postfix)
        postfix += nums[i]
