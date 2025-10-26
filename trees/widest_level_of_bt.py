from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widest_binary_tree_level(root:TreeNode) -> int:
    if not root:
        return 0
    
    max_width = 0
    queue = deque([(root, 0)]) # stores node and index together 
    print(queue)
    
    while queue: 
        level_size = len(queue) 
        leftmost_index = queue[0][1]
        rightmost_index = leftmost_index
        
        for _ in range(level_size):
            node, i = queue.popleft()
            print(node,i)
            if node.left:
                queue.append((node.left, 2 * i + 1))
            if node.right:
                queue.append((node.right, 2*i + 2))
            rightmost_index = i 
        max_width = max(max_width, rightmost_index - leftmost_index + 1)
    return max_width
    
    
root = [1,3,2,5,3,None,9]
print(widest_binary_tree_level(root))