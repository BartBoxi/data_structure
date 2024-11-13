class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
#
# def search(root, val):
#     while root:
#         if root.val == val:
#             return val
#         elif val < root.val:
#             root = root.left
#         else:
#             root = root.right
#     return None
#
#
#
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
#
#
# result = search(root, 2)
#
# print(result.val)
#
#
#
### now another task is just to check if the current val
## is inside of the tree
# if so, return yes, its there

def search(root, val):
    while root:
        if root.val == val:
            print(f"Yes")
            return # without this return its was going all the time
        elif val < root.val:
            root = root.left
        else:
            root = root.right
    print("No")

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

search(root, 7)


