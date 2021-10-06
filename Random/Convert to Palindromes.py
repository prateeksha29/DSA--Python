"""
Problem Description
Given a string A consisting only of lowercase characters, we need to check whether
it is possible to make this string a palindrome after removing exactly one character from this.
If it is possible then return 1 else return 0.

Problem Constraints
3 <= |A| <= 105
A[i] is always a lowercase character.

Output Format
Return 1 if it is possible to convert A to palindrome by removing exactly one character else return 0.

Example Input
Input 1:A = "abcba"
Output: 1
"""
# Two pointers
# Time: O(N)
# Space: O(1)
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        error = 0
        left, right = 0, len(A)-1

        while(left<=right):
            if A[left] == A[right]:
                left += 1
                right -= 1
            elif A[left] == A[right-1] and left <= right-1:
                error += 1
                right -= 1
            else:
                left += 1
                error += 1
            if error>=2:
                return 0
        return 1 if error<=1 else 0