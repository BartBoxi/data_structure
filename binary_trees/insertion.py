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
        root.right = insert(root.left, val)
    return root

def search(root, val):
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


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

insert(root, 8)

search(root, 8)

insert(root, 12)
search(root, 12)
search(root, 50)
