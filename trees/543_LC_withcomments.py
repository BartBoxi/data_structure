from typing import Optional # Import Optional for type hinting (specifies a parameter/return can be None)

# --- TreeNode Class Definition ---
class TreeNode:
    # Constructor for a tree node
    def __init__(self, val=0, left=None, right=None):
        self.val = val    # The value of the node
        self.left = left  # Pointer to the left child node
        self.right = right # Pointer to the right child node

# --- Main Solution Function ---
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # Initialize a variable to store the maximum diameter found so far.
    # The diameter will be updated within the recursive function.
    diameter = 0
    
    # Define a recursive helper function to calculate the longest path (height) 
    # starting from a given node.
    def longest_path(node):
        # Base case: If the node is None (we've gone past a leaf), the path length is 0.
        if not node:
            return 0
        
        # Use 'nonlocal' to indicate that we are modifying the 'diameter' variable 
        # defined in the outer scope (diameterOfBinaryTree function).
        nonlocal diameter
        
        # Recursively call the function for the left subtree to get the length 
        # of the longest path in the left subtree. This also calculates the height 
        # of the left subtree.
        left_path = longest_path(node.left)
        
        # Recursively call the function for the right subtree to get the length 
        # of the longest path in the right subtree. This also calculates the height 
        # of the right subtree.
        right_path = longest_path(node.right)

        # The diameter passing *through* the current 'node' is the sum of the longest 
        # paths from its left and right children (left_path + right_path).
        # We update the overall maximum diameter if this new path is longer.
        # Note: This path *doesn't* necessarily pass through the 'root' of the entire tree.
        diameter = max(diameter, left_path + right_path)
        
        # The function must return the longest path *from* the current 'node' downwards 
        # (its height), which is 1 (for the current edge) plus the maximum of the 
        # left_path or right_path. This value is used by the parent node to calculate 
        # its own diameter and height.
        return max(left_path, right_path) + 1
        
    # Start the recursive DFS traversal from the root of the tree.
    # This call calculates heights and updates the 'diameter' variable.
    longest_path(root)
    
    # After the DFS is complete, return the maximum diameter found.
    return diameter