s = "abc"
t = "apbqec"

class solution:
    def issubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i +=1
            j +=1

