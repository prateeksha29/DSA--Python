"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.



Example 1:

Input: n = 27
Output: true
"""

# Loop iteration
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while (n>1):
            if n%3 !=0:
                return False
            n = n//3

        return True


# Since 3 is prime, its max power should only be divisible by a power of 3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and (3 ** 19) % n == 0


# Can also be solved by base conversion
