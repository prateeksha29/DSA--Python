"""
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
"""

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        str_count = Counter(s)

        for i in range(len(s)):
            if str_count[s[i]] == 1:
                return i
        return -1
