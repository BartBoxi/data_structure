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
