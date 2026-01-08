class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
        ### left and right are the index of the nodes
        ### we need to reverse the list from the positon of the left node to the position of the right node 
        ### czyli gdy mam liste [1,2,3,4,5,6] i left = 2, right = 4 to mamy liste [1,4,3,2,5,6]
        ### left = 2, right =4 
        # czyli dla lewego rownego 2, prev = dummy ale next node bedzie prawy.next i curr bedzie rowny prawy 
        # no ale tu musze tez zrobic myk dla prawego ze prawy bedzie teraz sie rownal lewy, prawy prev bedzie lewy prev, a prawy next bedzie sie rowna lewy next
        # i musze wtedy lewy przesunac do przodu o 1 a prawy do tylu o 1 
        # czyli jestem na 3 dla lewego i 


        dummy = ListNode(0, head)
        before = dummy
        
        for i in range(left - 1):
            before = before.next
        
        tail = before.next
        curr = tail
        prev = None

        for i in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        before.next = prev 
        tail.next = curr
        return dummy.next

 
