"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
"""

# Hash Table
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        num_count = collections.Counter(nums)
        for key in num_count.keys():
            if num_count[key] == 1:
                return key


# XOR method (this method uses constant space)
# a XOR 0 = a
# a XOR a = 0
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a