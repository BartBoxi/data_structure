## First task for trees

### defining a TreeNode class
### Ex 1
class TreeNode:
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left_child = left
		self.right_child = right

node1 = TreeNode("B")
node2 = TreeNode("A")
root_node = TreeNode("A", node1, node2)
print(root_node)


# class Graph:
#   def __init__(self):
#     self.vertices = {}
#
#   def add_vertex(self, vertex):
#     self.vertices[vertex] = []
#
#   def add_edge(self, source, target):
#     self.vertices[source].append(target)


### Ex 2 Create Unidirected, Unweighted graph

# Nodes 0,1,2,3,
# Edges (0,1), (0,2), (1,2), (2,3)

# adj_matrix = [
# 	[0,1,1,0],
# 	[1,0,1,0],
# 	[1,1,0,1],
# 	[0,0,1,0]
# ]
#
# #check if edge (0,1) exists:
# print(adj_matrix[0][1]) #Output: 1

### ex 3 adjacency list

#Nodes A,B,C,D
#Edges: (A,B), (A,C), (B,C), (C,D)

### Typical Binary Tree representation

# class TreeNode:
# 	def __init__(self, val, left, right):
# 		self.val = val
# 		self.left = left
# 		self.right = right


### DFS Depth First search
#
# def dfs(node):
# 	if node == None:
# 		return
#
# 	dfs(node.left)
# 	dfs(node.right)
# 	return

## preorder traversal

# def preorder_dfs(node):
# 	if not node:
# 		return
# 	print(node.val)
# 	preorder_dfs(node.left)
# 	preorder_dfs(node.right)
# 	return


class TreeNode:
	def __init__(self, val=0):
		self.val = val
		self.left = None
		self.right = None


root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)

root.left = one
root.right = two

print(root.left.val)
print(root.right.val)



#
# def preorder_dfs(node):
# 	if not node:
# 		return
# 	print(node.val)
#
# 	for child in node.children:
# 		preorder_dfs(child)
# 	return
#
# def inorder_dfs(node):
# 	if not node:
# 		return
#
# 	if node.children:
# 		inorder_dfs(node.children[0])
#
# 	print(node.val)
#
# 	if len(node.children) > 1:
# 		for child in node.children[1:]:
# 			inorder_dfs(child)
# 	return
#
#
#
# node0 = TreeNode(0)
# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
#
# # Define relationships
# node0.children = [node1, node2]
# node1.children = [node3, node4]
# node2.children = [node5]
# node3.children = [] # Leaf node
# node4.children = [node6]
# node5.children = [] # Leaf node
# node6.children = [] # Leaf node
#
# #preorder_dfs(node0)
# inorder_dfs(node0)
#

