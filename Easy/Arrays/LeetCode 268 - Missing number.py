"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""

# Gauss Formula or Sum of first n numbers method
# Since the list of numbers should be 0 to n and one number is missing
# we use n * (n+1) / 2 to get the sum of all the numbers
# Subtract the sum of array,
# This returns the missing number
# O(n) and O(1)
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum



# Sort and search
# Time complexity is O(nlogn)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums= sorted(nums)
        range_ = len(nums)

        for i in range(range_ +1):
            if nums[i] != i:
                return i
            if i == len(nums)-1:
                return range_


# Bit Manipulation
# Take XOR of the array with the actual list of numbers which contains missing number, i.e. 0 to n
# Since a XOR a = 0
# Missing number will be returned
# O(n) and O(1)

class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing



