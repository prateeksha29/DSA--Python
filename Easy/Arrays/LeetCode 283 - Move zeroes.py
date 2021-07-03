"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

"""
Two Pointer approach
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[zero_pointer] == 0:
                nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
                zero_pointer += 1
            elif nums[zero_pointer] != 0:
                zero_pointer += 1


""" 
Pop and Append method
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        operations = 0
        index = 0
        while operations < len(nums):
            if nums[index] == 0:
                nums.append(nums.pop(index))
            else:
                index += 1
            operations += 1

