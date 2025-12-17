def mergeAlternately(word1: str, word2: str) -> str:
    ans = []
    i, j = 0, 0
    len1, len2 = len(word1), len(word2)

    while i < len1 or j < len2:
        if i < len1:
            ans.append(word1[i])
            i += 1
        if j < len2:
            ans.append(word2[j])
            j += 1
    return ''.join(ans)

word1 = "ab"
word2 = "pqrs"

print(mergeAlternately(word1, word2))

