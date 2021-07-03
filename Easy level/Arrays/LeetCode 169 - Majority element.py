"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
"""

# Create a dictionary of counter of the elements
# Return the key with maximum value
# Time complexity: O(n)
# Space Complexity: O(n)

import collections


class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# sort the array
# the element exist at nth or (n+1)th position
# Time complexity: O(nlogn)
# Space complexity: O(1)
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
