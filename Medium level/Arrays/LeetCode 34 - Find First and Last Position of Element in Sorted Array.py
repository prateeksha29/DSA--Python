"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

# Two pointers
# O(N) time and O(1) space
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        s, e = 0, len(nums) - 1

        while (s < e):
            if nums[s] == target and nums[e] == target:
                return [s, e]
            if nums[s] != target:
                s += 1
            if nums[e] != target:
                e -= 1
        if nums[s] == target:
            return [s, s]
        return [-1, -1]