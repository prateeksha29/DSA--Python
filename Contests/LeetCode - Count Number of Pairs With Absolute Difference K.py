"""
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
The value of |x| is defined as:
x if x >= 0.
-x if x < 0.

Example 1:
Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]

Example 2:
Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
"""
# Using hashmap
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 0
        pairs = 0
        hashmap = collections.Counter(nums)
        for num in nums:
            complement = abs(k-num)
            if complement in hashmap and abs(complement - num) == k:
                pairs += hashmap[complement]
        return pairs