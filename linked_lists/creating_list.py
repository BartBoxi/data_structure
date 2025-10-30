class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)

one.next = two
two.next = three
three.next = four
four.next = five

head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)

### example of getting a sum of all values from an integer linked list 

def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    return ans 

