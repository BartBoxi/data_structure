def convertToBase13(num):
    if num == 0:
        return "0"
    
    # digits for base 13 
    base13_digits = "0123456789ABC"
    digits = ""
    positive = abs(num)
    print(positive)
    
    while positive > 0:
        print(positive % 13)
        digits += base13_digits[positive % 13]
        print(digits)
        positive = positive // 13
        print(positive)
        

print(convertToBase13(48))