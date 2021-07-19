# Sorting
# o(nlogn) time
# constant space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


# Hashset
# O(n) time
# O(n) space
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)



# Flyod's cycle detection
# two pointers approach
# O(n) time and O(1) space
# function is nums[i] = val; nums[val] = val2. Since the numbers are in the range [1,n]
# Using slow and fast pointers finding the intersection point
# In next phase, restarting pointers from 0 and the intersection at the same pace
class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the "entrance" to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast