

def window(length, offset, lst):
    result = []
    i = 0
    while i + length <= len(lst):
        result.append(lst[i:i+length])
        i += offset
    return result


print(window(2, 1, [0,1,2,3,4]))

