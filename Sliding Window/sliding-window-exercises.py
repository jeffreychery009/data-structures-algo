# Problem 1
# Sliding Window Maximum Sum
# Find the maximum sum of a subarray of size k
# Here we use two pointers to keep track of the current sum and the maximum sum and a sliding window to keep track of the subarray
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxSum(nums, k):
    l = 0
    total = 0
    max_sum = float("-inf")

    for r in range(len(nums)):
        total += nums[r]
        if r - l + 1 > k:
            total -= nums[l]
            l += 1
        max_sum = max(total, max_sum)
    return max_sum


# Problem 2
# Find average of subarray of size k
# Here we use two pointers to keep track of the current sum and the average and a sliding window to keep track of the subarray
# Time Complexity: O(n)
# Space Complexity: O(1)
def findAverage(nums, k):
    l = 0
    total = 0
    result = []

    for r in range(len(nums)):
        total += nums[r]
        if r - l + 1 == k:
           average = total / k
           result.append(average)
           total -= nums[l]
           l += 1
    return result





