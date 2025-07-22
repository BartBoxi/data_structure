sentence = "leetcode"

def checkifPangram(sentence) -> bool:
    letters = set(sentence)
    if len(letters) == 26:
        return True
    else:
        return False



print(checkifPangram(sentence))