# Sliding Window

# Sliding Window is a technique used to solve problems that involve finding a subarray of a given array that satisfies a certain condition.
# The technique is to use two pointers to create a window that slides over the array to find the subarray.
# The window is a subarray of the given array that satisfies the condition.
# The window is created by moving the right pointer to the right and the left pointer to the right 
# until the condition is no longer satisfied.
# The window is then moved to the right until the condition is satisfied again.


# Brute Force Solution
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def containsDuplicatesBruteForce(nums, k):

    for L in range(len(nums)):
        for R in range(L+1, min(len(nums), L + k )):
            if nums[L] == nums[R]:
                return True
    return False


# Optimized Solution
# Time Complexity: 0(n)
# Space Complexity: 0(n)
# Here we use a two pointer approach and a hashset to efficiently look for duplicates in Big 0(1) fashion
# We use the right side as we go through the array to add numbers in the set if they haven't been seen before.
def containsDuplicates(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L > k:
            window.remove(nums[L])
        L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


# Sliding Window Minimum Sum
# Find the minimum sum of a subarray of size k
# Here we use two pointers to keep track of the current sum and the minimum sum and a sliding window to keep track of the subarray
# Time Complexity: O(n)
# Space Complexity: O(1)
def findShortest(nums, sum):
    L = 0
    total = 0
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]
        while total >= sum:
            total -= nums[L]
            L+=1
            length = min(length, R - L + 1)
    return 0 if length == float("inf") else length
        




        
        


