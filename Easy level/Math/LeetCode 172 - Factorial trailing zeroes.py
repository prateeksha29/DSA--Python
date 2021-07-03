"""
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?



Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 0
Output: 0
"""

# Counting the factors of multiples of 5
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        while (n > 0):
            zeroes += n // 5
            n = n // 5

        return zeroes
