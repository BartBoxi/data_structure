
def reverseString(s):
    left, right = 0, len(s) - 1 ## read it as left = 0, right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return s


s = ['a', 'b', 'c']
print(reverseString(s))