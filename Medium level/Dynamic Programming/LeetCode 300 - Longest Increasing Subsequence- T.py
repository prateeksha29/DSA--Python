"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

# DP
# Logic: initialize dp with 1 because all elements are atleast their own increasing subsequence
# bottom up approach: for each index, check with previous indices that if the previous number is smaller than current
# take the max(cur_dp, dp[prev] + 1)
# Time complexity: O(N^2)
# Space complexity: O(N)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]

        for n in range(1, len(nums)):
            for j in range(n):
                if nums[j] < nums[n]:
                    dp[n] = max(dp[n], dp[j] + 1)
        return max(dp)

# Two more methods on LeetCode
# One obtaining subsequence intelligently
# Using Binary Search