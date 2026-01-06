### Reverse linked list 
# head = [1,2,3,4,5]

# czyli mamy value i mamy next 
# czyli mozna zrobic two pointers z czego pierwszy bedzie od poczatku a drugi bedzie szedl od konca 
# iteratywnie to ineczej two pointers solution 


# curr = head
# prev = None

# while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt
# return prev

# # head = [1,2,3,4,5] 
# 1. curr = head
# prev = none

# nxt = curr.next --> head[0] -> 1 
# curr.next = prev -> prev = None 
# prev = curr -> head 
# curr = nxt -> czyli current 1 

# curr = 1
# prev = head

# 2. nxt = curr.next -> head[1] -> 2
#     curr.next = prev -> prev = head
#     prev = curr -> head[0] -> 1
#     curr = nxt -> czyli current 2

def ListNode(val=0, next=None):
    self.val = val
    self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None

    while curr: 
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev ### zwracamy prev poniewaz jest to nowy head 

head = [1,2,3,4,5]
print(reverseList(head))


    
