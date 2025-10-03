if __name__ == '__main__':
    s = input()
    alnum, alpha, digit, lower, upper = False, False, False, False, False
    for i in s:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
    print(alnum, alpha, digit, lower, upper, sep='\n')





