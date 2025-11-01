class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add_node(prev_node, node_to_add):
        node_to_add.next = prev_node.next
        prev_node.next = node_to_add
        


### if we have a pointer already then O(1)
# but if we dont have it and we need to find the place it will be O(n) because we need to iterate from the head