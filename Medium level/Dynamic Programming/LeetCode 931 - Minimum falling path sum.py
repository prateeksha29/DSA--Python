"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
"""

# Recursion with memoization
class Solution:
    def __init__(self):
        self.memo = {}

    def minPath(self, matrix, i, j):
        if i >= len(matrix):
            return 0
        if j >= len(matrix[0]) or j < 0:
            return 101

        num = matrix[i][j]
        if (i, j) in self.memo.keys():
            return self.memo[(i, j)]
        ans = min(self.minPath(matrix, i + 1, j) + num, self.minPath(matrix, i + 1, j + 1) + num,
                  self.minPath(matrix, i + 1, j - 1) + num)
        self.memo[(i, j)] = ans
        return ans

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        result = []
        for j in range(len(matrix[0])):
            res = self.minPath(matrix, 0, j)
            result.append(res)
        return min(result)

