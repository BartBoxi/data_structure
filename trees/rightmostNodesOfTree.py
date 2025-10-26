from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def rightmost_nodes_of_a_binary_tree(root: TreeNode):
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level_size - 1:
                    res.append(node.val)
        return res 
    

def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        parent = queue.popleft()
        
        if i < len(nodes) and nodes[i] is not None:
            parent.left = TreeNode(nodes[i])
            queue.append(parent.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            parent.right = TreeNode(nodes[i])
            queue.append(parent.right)
        i += 1
    
    return root


list = [1,2,3,None,5,None,4]
root_node = build_tree(list)
print(rightmost_nodes_of_a_binary_tree(root_node))
