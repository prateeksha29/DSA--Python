"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

from collections import Counter
# converting one string to dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)

        for i in t:
            if s_count[i] == 0:
                return False
            else:
                s_count[i] -= 1
        if sum(s_count.values())==0:
            return True
        return False



# Convering both strings to dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s and not t:
            return True

        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter


# Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False
