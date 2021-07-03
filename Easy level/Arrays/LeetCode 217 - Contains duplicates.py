"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
"""

# Using hashmap
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)
        a = sum(1 for i in num_count.values() if i > 1)
        if a>0:
            return True
        return False

# Using set function
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        return False
