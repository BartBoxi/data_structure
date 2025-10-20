from collections import TreeNode


### recursive method 
def invert_binary_tree(root: TreeNode):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root


### iterative method with stack 

def invert_binary_tree_iterative(root: TreeNode):
    if not root:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return root

