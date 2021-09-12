"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
"""

# Dp
# top down
# Time: O(T+N)
# Space: O(T)

class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        for t in range(target+1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t-num]
                else:
                    break
        return dp[target]