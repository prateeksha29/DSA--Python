"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

# Recursion
# Time: O(MxN)
# Space: O(1)
# Slow due to recursion stack
# There is only one path to reach the cell in the first row (keep going right)
# only one way to reach in the firest col (going down)
# we need to calculate for inner cells
# We can reach an inner cell from above col or row beside it
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


# DP
# using 2D matrix to store initial value of 1
class Solution:
    def uniquePaths(self, m, n):
        dp = [[1] * n for _ in range(m)]
        for col in range(m - 2, -1, -1):
            for row in range(n - 2, -1, -1):
                dp[col][row] = dp[col + 1][row] + dp[col][row + 1]

        return dp[0][0]
