


def isPalindrome(x:int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_num = 0
    
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
        print(reversed_num)
        print(x)
        
    return x == reversed_num or x == reversed_num // 10
    print(x)




print(isPalindrome(4224))