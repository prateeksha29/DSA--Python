"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.



Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""

# Using the mid point as the node in every recursion
class Solution:
    def constructTree(self, nums, left, right):
        if left > right: return None

        midpoint = left + (right - left) // 2
        node = TreeNode(nums[midpoint])
        node.left = self.constructTree(nums, left, midpoint - 1)
        node.right = self.constructTree(nums, midpoint + 1, right)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.constructTree(nums, 0, len(nums) - 1)