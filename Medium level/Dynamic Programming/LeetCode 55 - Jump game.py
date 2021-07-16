"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
# Recursion with memoization
# class Solution:
#     def jump(self,nums, i, dp):
#         if i in dp.keys():
#             return dp[i]
#         elif i+nums[i]>= len(nums)-1:
#             dp[i] =True
#             return True
#         else:
#             for val in range(1,nums[i]+1):
#                 prev = self.jump(nums, i+val, dp)
#                 if prev == True:
#                     dp[i] = True
#                     break
#             return dp[i]
#     def canJump(self, nums: List[int]) -> bool:
#         if len(nums) == 1:
#             return True
#         dp = {}
#         dp[0] = self.jump(nums,0,dp)
#         return dp[0]






# DP Bottom up approach
# eliminates recursive stack
# Time complexity : O(n^2)
# Space complexity: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if dp[i + j] == 1:
                    dp[i] = 1
                    break
        return dp[0] == 1


# Most optimized method
# Greedy approach
# Keep on shortening the array to the index if its possible to reach the end from that index
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if (i+nums[i] >= last):
                last = i
        return last==0

