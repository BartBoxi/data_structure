from collections import defaultdict
from typing import List

def minimumCardPickup(cards: List[int]) -> int:
    dic = defaultdict(int)
    print(dic)
    ans = float("inf")
    print(ans)

    for i in range(len(cards)):
        print(f"this is i {i}")
        if cards[i] in dic:
            ans =  min(ans, i - dic[cards[i]] + 1)
            print(f"this is ans if in dic{ans} ")

        dic[cards[i]] = i
        print(f"this is dic if not ans: {dic} ")

    return ans if ans < float("inf") else -1

cards = [1, 2, 6, 2, 1]

print(minimumCardPickup(cards))
