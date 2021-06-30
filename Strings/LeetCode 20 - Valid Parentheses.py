"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
"""

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        sign = {'(': ')',
                '{': '}',
                '[': ']'}

        stack = []
        close_stack = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            if i in [')', '}', ']']:
                if len(stack) != 0 and i == sign[stack[-1]]:
                    stack.pop()
                else:
                    close_stack.append(i)

        if len(stack) == 0 and len(close_stack) == 0:
            return True
        return False
