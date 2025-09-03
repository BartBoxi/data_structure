from collections import defaultdict
from typing import List

def minimumCardPickup(cards: List[int]):
    dic = defaultdict(list)
    for i in range(len(cards)):
        dic[cards[i]].append(i) ## here we are calling the value
                                # at specific index
    ###after this one that's how our dic will look like
    #dic = {1: [0, 4], 2: [1, 3], 6: [2]}

    ans = float("inf")  #so we are setting up this value to infitiy just as a trick to solve it
    for key in dic: # key = 2
        arr = dic[key] # = dic[1,3] ==> 2
        for i in range(len(arr) -1): # range(len(2 - 1)) ==> range(len(1))
            ans = min(ans, arr[i + 1] - arr[i] + 1) # we calculate from end ot begining
            ## With i = 0, this becomes: ans = min(ans, arr[1] - arr[0] + 1)
            ## ans = min(ans, 3 - 1, + 1)
            ## ans = min(ans, 3)

    return ans if ans < float("inf") else -1 # here we need to statement as it give answer only
### if the answer exist or if there is no ans then it will give us -1


cards = [1, 2, 6, 2, 1]

print(minimumCardPickup(cards))