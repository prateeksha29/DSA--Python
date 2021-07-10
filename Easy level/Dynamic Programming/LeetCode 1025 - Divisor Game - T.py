"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
"""

# Before the DP approach, Backtracking with recursion
# Time complexity is O(2^N)
# Overlapping sub-problems

# Below solution is recursion with memoization (DP) to solve overlapping problem
# Time complexity is O(N^3)
class Solution:
    def canWin(self, n, dp):
        if n == 1:
            return False
        if n in dp.keys():
            return dp[n]
        for x in range(1, n):
            if n%x == 0:
                if not self.canWin(n-x, dp):
                    dp[n] = True
                    return True
        dp[n] = False
        return False

    def divisorGame(self, n: int) -> bool:
        dp = {}
        return self.canWin(n, dp)


# Improving the DP solution by iterationg till sqrt(N) for factors
class Solution:
    def canWin(self, n, dp):
        if n == 1:
            return False
        if n in dp.keys():
            return dp[n]
        for x in range(1, int(math.sqrt(n) +1)):
            if n%x == 0:
                if not self.canWin(n-x, dp):
                    dp[n] = True
                    return True
                if x != 1 and not self.canWin(n-(n//x), dp):
                    dp[n] = True
                    return True
        dp[n] = False
        return False

    def divisorGame(self, n: int) -> bool:
        dp = {}
        return self.canWin(n, dp)


# Mathematical trick solution
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n%2 == 0
