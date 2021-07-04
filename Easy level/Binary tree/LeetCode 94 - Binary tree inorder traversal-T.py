"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursive solution
class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# Morris inorder traversal
# Dont have to use stack for goibg back to the root node
# set the right node link between predecessor of root and root
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        curr = root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return result

