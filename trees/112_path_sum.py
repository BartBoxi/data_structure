from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- The TreeNode Class ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(node: Optional[TreeNode], current_sum: int) -> bool: 
        if not node:
            return False
        if not node.left and not node.right:   ### czyli to musi byc leaf, czyli to automatycznie staje sie rozwiazanie dla leaf 
            return current_sum == targetSum ## tutaj wynik to bool 
        return dfs(node.left, current_sum) or dfs(node.right, current_sum)
    return dfs(root, 0) # roota bierzemy od pierwszej funkcji 







root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
targetSum = 22

print(hasPathSum(root, targetSum))


# TODO: Finish the function that will create a binary tree based on that notes:
#Start with the first element in the list — that’s your root node.

# Then, use a queue (like from collections.deque) to keep track of nodes whose children you still need to assign.

# For each node in the queue:

# Assign the next list element as its left child (if it isn’t None).

# Then assign the next element as its right child (if it isn’t None).

# Each time you create a new child node, add it to the queue.

# Continue until you’ve processed all the elements in the list.


