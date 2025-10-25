


def isPalindrome(x:int) -> bool:
    if x >= 0:
        rev_num = int(str(x)[::-1])
        if x == rev_num:
            return True
        else:
            return False
    else:
        return False
    
    
x = 0
print(isPalindrome(x))

################################

