from collections import defaultdict
from typing import List

def minimumCardPickup(cards: List[int]):
    dic = defaultdict(list)
    for i in range(len(cards)):
        dic[cards[i].append(i)] ## here we are calling the value
                                # at specific index

        print(dic)


cards = [1, 2, 6, 2, 1]

print(minimumCardPickup(cards))