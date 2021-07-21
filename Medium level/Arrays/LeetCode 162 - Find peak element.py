"""
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""
# Iterative Binary search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while(l<r):
            mid = (l+r)//2
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid
        return l



# Recursive binary search
class Solution:
    def binarySearch(self, nums, l, r):
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:
            return self.binarySearch(nums, mid + 1, r)
        return self.binarySearch(nums, l, mid)

    def findPeakElement(self, nums):
        return self.binarySearch(nums, 0, len(nums) - 1)