class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def search(root,val):
    while root:
        if root.val == val:
            print("Yes")
            return True
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    print("No")
    return False

def minval(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def remove(root, val):
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        else:
            minNode = minval(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

root = TreeNode(1)
insert(root,2)
insert(root, 3)
insert(root, 4)
remove(root, 2)
inorder_traversal(root)
