"""
Problem Description
Given a string A of parantheses  ‘(‘ or ‘)’.
The task is to find minimum number of parentheses ‘(‘ or ‘)’ (at any positions) we must add to make the resulting parentheses string valid.
An string is valid if:
Open brackets must be closed by the corresponding closing bracket.
Open brackets must be closed in the correct order.

Problem Constraints
1 <= |A| <= 105
A[i] = '(' or A[i] = ')'

Example 1:
Input: [')(']
Output: 2
"""

# using stacks
# Time : O(N)
# space: O(N)
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        open_stack = []
        close_stack = []

        for s in A:
            if s == '(':
                open_stack.append(s)
            elif s == ')' and len(open_stack) == 0:
                close_stack.append(')')
            else:
                open_stack.pop()
        return len(open_stack) + len(close_stack)