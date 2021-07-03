"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
"""

# Using hashmap and intersection
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_count1 = Counter(nums1)
        num_count2 = Counter(nums2)

        res = list(set(nums1).intersection(set(nums2)))

        final = []
        for num in res:
            count = min(num_count1[num], num_count2[num])
            arr = [num] * count
            final.extend(arr)
        return final