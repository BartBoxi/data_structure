### leetcode 92 

# Given the head of a singly linked list and two integers left and right where 
# left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


### lista [1,2,3,4,5]
#            L   R --> right - left - tutaj bedzie moj range
# dummy = 0 bedzie tylko po to aby zwrocic wszystko od dummy.next 



def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    
    for _ in range(left - 1):
        pre = pre.next  ## sobie przesuwamy pre na 1
        
        
        curr = pre.next  ## tutaj jestem 2
        
    
    for _ in range(right - left):
        next_node = curr.next # jestem na 3   
        
        curr.next = next_node.next # strzalka z wezla 2 wskazuje na 4 - czytamy od prawej do lewej 4 --> czyli curr czyli 2 trzymaj za reke 4 (bo jakby curr.next to prawa reka dwojki)
        
        # obecna sytuacja 
        
        # 
        # next_node = 3 
        # 2 --> 4 
        
        next_node.next = pre.next  # trojka ma trzymac za reke 2
        
        ## obecna sytuacja 
        
        #next_node = 3
        # 2 --> 4
        #  3 --> 2 
        
        # 3 > 2 > 4 
        
        pre.next = next_node 
        
    return dummy.next 

    
        








head = [1,2,3,4,5]

left = 2
right = 4