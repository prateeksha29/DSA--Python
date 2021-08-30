"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

# Brute force with two pass on the array
# Time complexity: O(N^2)
# Space: O(1)
# Keeping max of the prod starign from ith number
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        result = nums[0]

        for i in range(len(nums)):
            accu = 1
            for j in range(i, len(nums)):
                accu *= nums[j]
                result = max(result, accu)

        return result



# Using Dynamic Programming to keep track of current max product
# Tricky part is handling the negative numbers
# So, we keep track of minimum so far so that it might turn into max if another negative num is encountered
# Time: O(N)
# Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max_so_far = min_so_far = nums[0]
        for num in nums[1:]:
            temp_max = max(num, max_so_far * num, min_so_far * num)
            min_so_far = min(num, max_so_far * num, min_so_far * num)

            max_so_far = temp_max
            result = max(max_so_far, result)

        return result

