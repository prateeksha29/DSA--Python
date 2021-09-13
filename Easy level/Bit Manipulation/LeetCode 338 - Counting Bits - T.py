"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

# DP
# space: O(N)
# time: O(N)
# logic: Since, the binary representation of numbers between 2's powers is very similar and differs by just one 1.
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n+1)]
        prev_pow = 1
        for i in range(1, n+1):
            if prev_pow * 2 == i:
                prev_pow = i
                dp[i] = 1 + dp[i-prev_pow]
            else:
                dp[i] = 1 + dp[i-prev_pow]
        return dp