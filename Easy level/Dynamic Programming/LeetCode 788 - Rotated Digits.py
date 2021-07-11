"""
x is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number n, how many numbers x from 1 to n are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
"""

# bruteforce using hashmap
class Solution:
    def rotatedDigits(self, n: int) -> int:
        rot_dict = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

        result = 0
        for i in range(n + 1):
            cur = i
            rot_num = 0
            compare = True
            p = 0
            while (cur != 0):
                dig = cur % 10
                if dig not in rot_dict.keys():
                    cur = 0
                    compare = False
                else:
                    num = rot_dict[dig]
                    rot_num += num * pow(10, p)
                    p += 1
                    cur //= 10
            if compare:
                if rot_num != i:
                    result += 1
        return result


