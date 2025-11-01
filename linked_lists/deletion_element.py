class ListNode: 
    def __init__(self,val):
        self.val = val
        self.next = None
        

def delete_node(prev_node):
    prev_node.next = prev_node.next.next
    
    