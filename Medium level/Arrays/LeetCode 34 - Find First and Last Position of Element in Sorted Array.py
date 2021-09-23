"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

# Two pointers
# O(N) time and O(1) space
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        s, e = 0, len(nums) - 1

        while (s < e):
            if nums[s] == target and nums[e] == target:
                return [s, e]
            if nums[s] != target:
                s += 1
            if nums[e] != target:
                e -= 1
        if nums[s] == target:
            return [s, s]
        return [-1, -1]


# Binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]

        upper_bound = self.findBound(nums, target, False)

        return [lower_bound, upper_bound]

    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:

        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)

            if nums[mid] == target:

                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:

                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid

                    # Search on the right side for the bound.
                    begin = mid + 1

            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1

        return -1