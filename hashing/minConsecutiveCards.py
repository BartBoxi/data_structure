from collections import defaultdict
from typing import List

def minimumCardPickup(cards: List[int]):
    dic = defaultdict(list)
    for i in range(len(cards)):
        dic[cards[i]].append(i) ## here we are calling the value
                                # at specific index

    ans = float("inf")
    for key in dic:
        arr = dic[key]
        for i in range(len(arr) -1):
            ans = min(ans, arr[i + 1] - arr[i] + 1)

    return ans if ans < float("inf") else -1


cards = [1, 2, 6, 2, 1]

print(minimumCardPickup(cards))