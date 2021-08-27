"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
"""
# Binary search
# Time complexity: O(log N)
# Space complexity: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[-1] == len(arr):
            return len(arr) + k

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            missing = self.compute(arr[mid], mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        if right == -1:
            return k

        return arr[right] + k - self.compute(arr[right], right + 1)

    def compute(self, actual, expected):
        return actual - expected

