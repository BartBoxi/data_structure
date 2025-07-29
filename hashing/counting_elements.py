### Here the task is find all the numbers x + 1
from typing import List

def countElements(arr: List[int]) -> int:
    new_set = set(arr)
    ans = 0
    for i in arr:
        if i + 1 in new_set:
            ans += 1
    return ans



arr = [1,1,3,3,5,5,7,7]

print(countElements(arr))