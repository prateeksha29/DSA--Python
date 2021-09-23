"""
Given a binary tree root, a node X in the tree is named good if
in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
"""

# Recursive Depth first search
# Time: O(n)
# Space: O(N)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 1
        self.check_max(root.left, root.val)
        self.check_max(root.right, root.val)

        return self.result

    def check_max(self, root, cur_max):
        if root is None:
            return
        if root.val >= cur_max:
            cur_max = root.val
            self.result += 1
        self.check_max(root.left, cur_max)
        self.check_max(root.right, cur_max)




# iterative DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float("-inf"))]
        num_good_nodes = 0
        while stack:
            node, max_so_far = stack.pop()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.left:
                stack.append((node.left, max(node.val, max_so_far)))
            if node.right:
                stack.append((node.right, max(node.val, max_so_far)))

        return num_good_nodes


# BFS
# Time: O(N)
# Space: O(N)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good_nodes = 0
        queue = deque([(root, float("-inf"))])
        while queue:
            node, max_so_far = queue.popleft()
            if max_so_far <= node.val:
                num_good_nodes += 1
            if node.right:
                queue.append((node.right, max(node.val, max_so_far)))
            if node.left:
                queue.append((node.left, max(node.val, max_so_far)))

        return num_good_nodes