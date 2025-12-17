def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    ### input  head = [1,2,3,4,5] left = 2, right = 4
    ### output [1,4,3,2,5]
    
    ### so we need to recursive solution first:
    # first remove the left node and store it as the removed node
    # then store the prev for the removed node and next one 