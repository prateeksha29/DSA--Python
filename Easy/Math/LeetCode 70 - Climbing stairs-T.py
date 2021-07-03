"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# dynamic programming approach
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        num_dict = {1: 1, 2: 2}

        for i in range(3, n + 1):
            num_dict[i] = num_dict[i - 1] + num_dict[i - 2]

        return num_dict[n]

# Fibonacci
# DP with constant memory
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second

            first = second
            second = third

        return second
