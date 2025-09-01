from collections import defaultdict
from typing import List

def isAnagram(strs:List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            #print(key)
            groups[key].append(s)
            #print(groups)

        return list(groups.values())


strs = ["eat","tea","tan","ate","nat","bat"]

print(isAnagram(strs))