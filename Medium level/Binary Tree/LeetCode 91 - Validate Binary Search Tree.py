"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [2,2,2]
Output: false
"""

# Iterative Inorder traversal
# time: O(N)
# space: O(N)
# uses the least space because we only need to record the previous value
class Solution:
    def isValidBST(self, root):
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True



# Recursive Inorder Traversal
class Solution:
    def isValidBST(self, root):
        def inOrder(node):
            if not node:
                return True
            if not inOrder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inOrder(node.right)
        self.prev = -math.inf
        return inOrder(root)



# Traversal using lower and upper bounds
# Uses a little more space than inorder traversal
class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]

        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))

        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            return ( validate(node.left, low, node.val)  and
                  validate(node.right, node.val, high))

        return validate(root)