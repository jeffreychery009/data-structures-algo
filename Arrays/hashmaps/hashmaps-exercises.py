# Problem 1
# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class solution:
    def hasduplicate(self, nums: list[int]) -> bool:
        if len(nums) == 0:
            return False

        countmap = {}
        for num in nums:
            if num not in countmap:
                countmap[num] = 1
            else:
                return True
        return False
    
# Problem 2
# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = [0] * 26
        for i in range(len(s)):
            map[ord(s[i]) - ord('a')] += 1
            map[ord(t[i]) - ord('a')] -= 1

        for val in map:
            if val != 0:
                return False
        return True

#test cases
print(Solution().isAnagram("anagram", "nagaram")) # True
print(Solution().isAnagram("rat", "car")) # False

# Problem 3
# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in map:
                return [map[diff], i]
            map[num] = i
        return []
        
        
        
