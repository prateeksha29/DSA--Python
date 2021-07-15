"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
Return the number of bulbs that are on after n rounds.

Example 1:
Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.
"""
# using perfect square property
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)


# For loop to check if the number is perfect square
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return n
        result = 0
        for i in range(1,n+1):
            for div in range(int(math.sqrt(i))+1):
                if div*div == i:
                    result += 1
                    break

        return result