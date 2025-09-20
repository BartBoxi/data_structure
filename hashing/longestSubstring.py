from typing import List
from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_length = 0
    hashset = set()

    for right in range(len(s)):
        if s[right] in hashset:
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
        hashset.add(s[right])
        current_length = (right  - left + 1)
        max_length = max(current_length, max_length )

    return max_length


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
