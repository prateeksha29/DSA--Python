"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

# Recursion with memoization
class Solution:
    def __init__(self):
        self.memo = {}
    def robFrom(self, i, nums):
        if i >= len(nums):
            return 0
        if i in self.memo.keys():
            return self.memo[i]
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        self.memo[i] = ans
        return ans

    def rob(self, nums):
        return self.robFrom(0, nums)


# Dynamic Programming
class Solution:

    def rob(self, nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):

            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])

        return maxRobbedAmount[0]



# DP with constant space
class Solution:

    def rob(self, nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])

            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next


