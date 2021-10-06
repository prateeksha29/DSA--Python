"""
You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input Format:
The first and the only argument contains an integer A, the number of steps.

Output Format:
Return an integer, representing the number of ways to reach the top.

Constrains:
1 <= A <= 36
Example :

Input 1: A = 3
Output 1:3
Explanation 1:
[1 1 1], [1 2], [2 1]
"""
class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
        dp = [-1] *len(range(A))
        return self.recur(0, A, dp)

    def recur(self, curr, target, dp):
        if curr > target:
            return 0
        if curr == target -1 or curr == target:
            return 1
        if dp[curr] != -1:
            return dp[curr]
        else:
            step1 = self.recur(curr+1, target, dp)
            step2 = self.recur(curr+2, target, dp)
            dp[curr] = step1 + step2
            return dp[curr]