class ListNode(self, val):
    self.val = val
    self.next = None
    self.prev = None

node_1 = ListNode(1)
self.head.next = node_1
node_1.prev = self.head

node_2 = ListNode(2)
node_2.prev = node_1
node_1.next = node_2

node_3 = ListNode(3)
node_3.prev = node_2
node_2.next = node_3

node_3.next = self.tail
tail.prev = node_3 
