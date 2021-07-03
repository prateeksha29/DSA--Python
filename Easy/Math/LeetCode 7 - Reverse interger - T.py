"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Constraints:
-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        abs_num = abs(x)
        result = 0

        while (abs_num > 0):
            rem = abs_num % 10
            result = result * 10 + rem
            abs_num //= 10

        if x < 0:
            result = result * -1

        if not pow(-2, 31) < result < (pow(2, 31) - 1):
            return 0

        return result