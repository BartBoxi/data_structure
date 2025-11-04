from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None 
        
        arr = [head]
        while arr[-1].next:
            arr.append[arr[-1].next]
        return arr[len[arr] // 2] ### have to use floor division always here 
    



