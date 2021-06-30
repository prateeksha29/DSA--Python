"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().



Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
"""

# Writing from scratch without using any Python function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle in haystack:
            for i in range(len(haystack)-len(needle)+1):
                temp_s = haystack[i:i+len(needle)]
                if needle in temp_s:
                    return i
        else:
            return -1


# Using .index to find the index of the sub string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1