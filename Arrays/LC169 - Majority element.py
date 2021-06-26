"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
"""

# Create a dictionary of counter of the elements
# Return the key with maximum value

from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        return max(num_dict, key=num_dict.get)
