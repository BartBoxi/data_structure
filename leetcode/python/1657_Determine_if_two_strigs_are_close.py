from collections import Counter


def closeStrings(word1:str, word2: str) -> bool:
    seen1 = {}
    seen2 = {}
    
    # if len(word1) == len(word2):
    #     for i in word1:
    #         if i not in seen1:
    #             seen1[i] = 1
    #         else:
    #             seen1[i] += 1
        
    #     for j in word2:
    #         if j not in seen2:
    #             seen2[j] = 1
    #         else:
    #             seen2[j] +=1 
        
    #     if seen1.keys() == seen2.keys():
    #         if sorted(seen1.values()) == sorted(seen2.values()):
    #             return True
    #         else:
    #             return False
    # return False


# mozna jeszcze uzyc countera 

    if len(word1) != len(word2):
        return False 

    seen1 = Counter(word1)
    seen2 = Counter(word2)

    if seen1.keys() == seen2.keys():
        if sorted(seen1.values()) == sorted(seen2.values()):
            return True
        else:
            return False
    return False


word1 = "cabbba"
word2 = "abbccc"

print(closeStrings(word1,word2))
