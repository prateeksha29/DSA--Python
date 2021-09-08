"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
# Recursive
# create a node called 'Output' with same root value
# recursively set its left and right nodes
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        output = TreeNode(root.val)
        output.left = self.invertTree(root.right)
        output.right = self.invertTree(root.left)

        return output


# Iterative solution
# Using queue
# we create a queue to store nodes whose left and right child have not been swapped yet.
# Initially, only the root is in the queue.
# As long as the queue is not empty, remove the next node from the queue, swap its children, and add the children to the queue.
# Null nodes are not added to the queue.
# Eventually, the queue will be empty and all the children swapped, and we return the original root.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        qu = deque([root])
        while qu:
            node = qu.popleft()
            if node:
                if not node.left and not node.right: #if leaf node, continue to next iteration
                    continue
                if node.left or node.right: #swap left node to right and vice versa
                    tmp=node.left
                    node.left=node.right
                    node.right=tmp
                qu.append(node.left)
                qu.append(node.right)
        return root