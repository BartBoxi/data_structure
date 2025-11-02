### task is to find the middle value in the linked list which is odd 

def get_middle(head):
    length = 0 
    dummy = head
    while dummy:
        length += 1
        dummy = dummy.next
        
    for _ in range(length//2):
        head = head.next
    return head.val 

####. more elegant solution with fast and slower technique 

def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


