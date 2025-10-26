def romantoint(s:str) -> int:
    roman = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    solution = 0
    prev_val = 0
    
    for i in range(len(s)-1,-1,-1):
        curr_val = roman[s[i]]
        if curr_val < prev_val:
            solution -= curr_val
            prev_val = curr_val
        else:
            solution += curr_val
            prev_val = curr_val
    return solution
    

    
    
    

s = "MCMXCIV"
print(romantoint(s))


###
# I I I V L 

# MCMXCIV 
# V I C X C M M 
# V > I 