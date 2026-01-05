### we are having two sorted linked lists and we need to merge them into one sorted linked list
## list 1 and list 2

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    final_list = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        print(list1[i], list2[j])
        print(i,j)
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        else:
            final_list.append(list2[j])
            j += 1
        
    while i < len(list1): ### why this works because e.g when we are comparing list1 5 and list2 3 and 4 we are finsihing list2
        ## but we are never reaching to the end of len(list1) so we are adding 5 to the final list until the len(list1) is met. 
        final_list.append(list1[i])
        i += 1
    
    while j < len(list2):
        final_list.append(list2[j])
        j += 1
    
    return final_list

list1 = [1,2,5,6,7,8]
list2 = [1,3,4]
print(mergeTwoLists(list1, list2))



# dlaczego mam odpowiedz [1, 2, 1, 2, 4, 1, 3, 4] ? 



