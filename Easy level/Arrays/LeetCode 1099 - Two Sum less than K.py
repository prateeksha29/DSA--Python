"""
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

Example 1:
Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 1000
1 <= k <= 2000
"""
# Counting sort approach
# using the fact that nums[i]<=1000
# So creating a count array of numbers till 1000 and checing their sum
# O(n+m) time complexity
# O(m) space
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        count = [0] * 1001
        for num in nums:
            count[num] += 1
        lo = 1
        hi = min(k - 1, 1000)
        while lo <= hi:
            if lo + hi >= k or count[hi] == 0:
                hi -= 1
            else:
                if count[lo] > (0 if lo < hi else 1):
                    answer = max(answer, lo + hi)
                lo += 1
            if lo > k / 2:
                break
        return answer




# Two pointers
# i<j can also mean j < i. so, basically the question means i != 1
# hence the question can be solved after sorting the array
class Solution:
    def twoSumLessThanK(self, nums, k):
        answer = -1
        nums.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            sum_ = nums[left] + nums[right]
            if sum_ < k:
                answer = max(answer, sum_)
                left += 1
            else:
                right -= 1
            if nums[left] > k / 2:
                break
        return answer


# Binary search
# O(nlogn) time
# O(log n) space
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        nums.sort()
        for i in range(len(nums)):
            j = bisect_left(nums, k - nums[i], i + 1) - 1
            if j > i:
                answer = max(answer, nums[i] + nums[j])
        return answer
