### we are having two sorted linked lists and we need to merge them into one sorted linked list
## list 1 and list 2

# def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
#     final_list = []
#     i = 0
#     j = 0

#     while i < len(list1) and j < len(list2):
#         print(list1[i], list2[j])
#         print(i,j)
#         if list1[i] < list2[j]:
#             final_list.append(list1[i])
#             i += 1
#         else:
#             final_list.append(list2[j])
#             j += 1
        
#     while i < len(list1): ### why this works because e.g when we are comparing list1 5 and list2 3 and 4 we are finsihing list2
#         ## but we are never reaching to the end of len(list1) so we are adding 5 to the final list until the len(list1) is met. 
#         final_list.append(list1[i])
#         i += 1
    
#     while j < len(list2):
#         final_list.append(list2[j])
#         j += 1
    
#     return final_list

# alternative solution might be with use of final_list.extend(list1[i:]) final_list.extend(list2[j:])







### rozwiazanie dla ListNodes: 
from typing import Optional

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val: 
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    current.next = list1 if list1 else list2
    return dummy.next


def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:                    #current = ListNode(0)
        current.next = ListNode(val) #current.next = ListNode(1)
        current = current.next        # current = current.next lub po prostu ListNode(val)
    return dummy.next               # dummy.next = ListNode(1)

list1 = [1,2,5,6,7,8]

#creation of linked lists 

list1_linked = create_linked_list(list1)

# list2 = [1,3,4]
print(mergeTwoLists(    list1, list2))

