from typing import List
from collections import defaultdict

def canConstruct(ransomNote: str, magazine: str) -> bool:
    dic = defaultdict(int)
    for char in ransomNote:
        dic[char] += 1


    dic2 = defaultdict(int)
    for char in magazine:
        dic2[char] += 1


    print(dic)
    print(dic2)


    ans = False
    for key in dic:
        if key in dic2 and dic[key] == dic2[key]:
            ans = True
        else:
            ans = False
    return ans



ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))