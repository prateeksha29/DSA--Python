"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = [[1]]

        for i in range(1, numRows):
            res = [1, 1]
            if i >= 2:
                for j in range(1, i):
                    val = final[i - 1][j - 1] + final[i - 1][j]
                    res.insert(j, val)
            final.append(res)
        return final