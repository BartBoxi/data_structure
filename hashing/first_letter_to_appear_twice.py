def repeatedCharacter(s:str) -> str:
    for i in range(len(s)):
        c = s[i]
        for j in range(len(s)):
            if s[j] == c:
                return c
        return ""



s = "babajaga"
print(repeatedCharacter(s))