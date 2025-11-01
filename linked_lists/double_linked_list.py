class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    