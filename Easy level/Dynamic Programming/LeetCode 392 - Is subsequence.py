"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""

# Two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) ==0:
            return True
        s_idx = 0
        for i in range(len(t)):
            if s[s_idx] == t[i]:
                s_idx += 1
            if s_idx == len(s):
                return True
        return s_idx == len(s)



# recursion
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        else:
            return self.isSubsequence(s, t[1:])
