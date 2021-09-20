"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in
T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
"""
# Recursive approach
# time and space: O(N)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val > parent_val and q_val >parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# Iterative approach
# Time and space: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        p_val = p.val
        q_val = q.val

        node = root

        while node:
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node