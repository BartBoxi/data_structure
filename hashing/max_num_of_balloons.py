def maxBalloon(text:str) -> int:
    counts = {
        'b' : 0,
        'a': 0,
        'l' : 0,
        'o': 0,
        'n' :0
    }


    for char in text:
        if char in counts:
            counts[char] += 1

    counts['l'] = counts['l'] // 2 ### dzielenie bez reszty
    counts['o'] = counts['o'] // 2

    return min(counts.values())





print(maxBalloon("balon"))









