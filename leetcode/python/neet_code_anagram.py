def isAnagram(s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[i] = s[i]
        
        for j in range(len(t)):
            t_count[j] = t[j]
        
        print(sorted(s_count.values()))
        print(sorted(t_count.values()))
        return sorted(s_count.values()) == sorted(t_count.values()) 

s = "racecar"

t = "carrace"


print(isAnagram(s, t))