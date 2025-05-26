### Task   Minimum Depth of Binary Tree

### Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#

import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left) ### we needed to add edge cases when there is no left or right root
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left, right) + 1




