from collections import defaultdict


def numJewelsInStones(jewels:str, stones:str):
    jewels = list(jewels)
    stones = list(stones)

    print(jewels)
    ans = 0
    for stone in stones:
            if stone in jewels:
                ans += 1
    return ans





jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))



