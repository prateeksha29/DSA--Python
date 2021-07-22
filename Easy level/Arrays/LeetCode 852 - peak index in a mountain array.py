"""
Let's call an array arr a mountain if the following properties hold:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Example 1:
Input: arr = [0,1,0]
Output: 1
"""
# binary search
class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 1
        l, r = 0, len(nums) - 1

        while (l < r):
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif nums[mid] < nums[mid - 1]:
                r = mid
        return l

