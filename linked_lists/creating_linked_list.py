class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
# Write your code here
# Try creating 1 <-> 2 <-> 3
# Test with print()

head = ListNode("head")
tail = ListNode("tail")

head.next = tail
tail.prev = head

node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)

head.next = node_1
node_1.prev = head 

node_1.next = node_2
node_2.prev = node_1

node_2.next = node_3
node_3.prev = node_2

node_3.next = tail
tail.prev = node_3

current = node_1
while current is not tail:
    print(current.val, end = " ")
    current = current.next 
print("\n")
    
