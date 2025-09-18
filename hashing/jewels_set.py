
def numJewelsInStones(jewels:str, stones:str):
    jset = set(jewels)
    print(jset)
    return sum(s in jset for s in stones)

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
