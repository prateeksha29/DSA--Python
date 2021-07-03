"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

# using Hashset
class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while (n != 1):
            current = n
            sum_ = 0
            while (current != 0):
                current, digit = divmod(current, 10)
                sum_ += digit ** 2
            if sum_ in hashset:
                return False
            hashset.add(sum_)
            n = sum_

        return True


# Two pointers
# FLoyd's Cycle finding algo
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            sum_ = 0
            while number != 0:
                number, digit = divmod(number, 10)
                sum_ += digit ** 2

            return sum_

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1