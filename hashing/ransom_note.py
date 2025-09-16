from typing import List
from collections import defaultdict

### Note: this solution needs improvements as it is probably not asking about the count of letters in ransom
### but rather if the same char appeared in magazine e.g. "bg" in magazine "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"



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
        if key in dic2 and dic[key] <= dic2[key]:
            ans = True
        else:
            ans = False
            break
    return ans



ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"


print(canConstruct(ransomNote, magazine))