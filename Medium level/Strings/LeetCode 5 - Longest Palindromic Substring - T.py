"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "ac"
Output: "a"
"""

# Time complexity: O(N^2)
#Space: O(1)
#using the fact that the palindromes are symmetric around center
class Solution:
    def expandCentre(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        start = 0
        end = 0

        for i in range(len(s)):
            len_odd = self.expandCentre(s, i, i)
            len_even = self.expandCentre(s, i, i + 1)
            max_len = max(len_odd, len_even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end + 1]
