### task is In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

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





