"""

"""
# Using sort
# time complexity: O(NlogN)
# Space: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# Using heap
# returning the last element of the kleargest heap
# Time: O(NkogK)
# Space:O(K)
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

# Quickselect algorithm
# Time: O(N) on an average and O(N^2) worst case
# Space: O(1)
# Logic: initialize pivot at last number of the array
# After first pivot position is identified, compare k with pivot position
# and sort the only half where k lies
class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)