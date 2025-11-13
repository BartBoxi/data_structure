### First we need to create a ListNode so code to create a linked list
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


### here we got function to reverse a linked list 

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev # here is the moment we are switching the direction for that linked list
        prev = curr
        curr = next_node # and we using next_node because with the direction switch we are losing the connection to curr.next 
    return prev

### helper function for printing the linked list 

def print_list(head):
    current = head
    values = []
    while current:
        values.append(str(current.val))
        current = current.next
    print("->".join(values))

if __name__ == "__main__":
    
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    head_node = ListNode(1, node2)
    
    
    head_original = ListNode(1, ListNode(2, ListNode(3)))
    print_list(head_original)
    

    new_head = reverse_list(head_node)
    print_list(new_head)