"""
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
"""

# Using Stack
# Time Complexity: O(N)
# Space complexity: O(N)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        L=[c for c in s if c.isalpha()]
        o=''
        for c in s:
            o+=c if not c.isalpha() else L.pop()
        return o


# Using reverse pointer
# time: O(N)
# Space: O(N)
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ans = []
        j = len(S) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)

        return "".join(ans)





