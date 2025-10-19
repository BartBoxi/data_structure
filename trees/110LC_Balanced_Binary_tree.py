# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from binary_trees.LC700 import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(root):
            if root is None:
                return 0
            left_height = checkHeight(root.left)
            right_height = checkHeight(root.right)
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        if checkHeight(root) == -1:
            return False
        else:
            return True





