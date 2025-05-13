# Problem 1
# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class solution:
    def hasduplicate(self, nums: list[int]) -> bool:
        if len(nums) == 0: # Edge case
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
        if len(s) != len(t): # Edge case
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
        
        
        
# Problem 4
# Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for c in str:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            res[key].append(str)
        return res.values()
