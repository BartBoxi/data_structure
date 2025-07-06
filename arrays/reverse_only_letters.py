def reverse_only_letters(s: str):
    chars = list(s)
    left = 0
    right = len(s) -1


    while left < right:
        if chars[left].isalpha() and chars[right].isalpha():
            chars[left], chars[right] = chars[right], chars[left]
            left +=1
            right -=1
        elif not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
    return ''.join(chars)




s = "a-b1221212C-dEf-ghIj"
print(reverse_only_letters(s))

