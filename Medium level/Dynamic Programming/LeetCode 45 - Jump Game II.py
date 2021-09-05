"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

# DP
# Time: O(N^2)
# Space: O(N)
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [1001]*len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] != 0:
                val = [dp[i+j]+1 for j in range(1, nums[i]+1) if (i+j) < len(nums)]
                dp[i] = min(val)

        return dp[0]


# Greedy solution
# We define window of jumps for farthest from a point
# We only add a jump if we cross that window
# two variables: jumps, current_jump_end
# Time: O(N)
# Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
            jumps = 0
            current_jump_end = 0
            farthest = 0
            for i in range(len(nums) - 1):
                farthest = max(farthest, i + nums[i])
                if i == current_jump_end:
                    jumps += 1
                    current_jump_end = farthest
            return jumps