"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
and you need to find the kth smallest frequently, how would you optimize?
"""
# Using inorder traversal
# Time: O(N)
# Space: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if root is None:
            return []
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = self.inOrder(root)
        return stack[k-1]


# Suing iterative Inorder traversal
# no need to build the entire traversal
# one can stop after the kth element
# Implementation logic: Keeps going left till the lowest node
# then start popping and decresing the k
# if k is not 0, take the right node of this lowest left leaf and append it to the stack
# and keep iterationg through it, till k=0
# when k=0, return root.val
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right