"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnTitle = "A"
Output: 1
"""

## Right to left iteration
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = ord("A")-1
        if len(columnTitle)>1:
            val = 0
            for i in range(len(columnTitle)-1, -1,-1):
                base_val = ord(columnTitle[i])-base
                val += base_val * pow(26, len(columnTitle)-1-i)
            return val


        else:
            return ord(columnTitle)-base


## Left to right iteration
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for c in s:
            d = ord(c)-ord('A')+1
            result = result*26+d
        return result