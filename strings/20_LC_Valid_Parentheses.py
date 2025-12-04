
"""
Determines if the input string has valid parentheses.

Steps:
1. Initialize an empty stack.
2. Iterate through the input string character by character.
3. If the character is an opening bracket '(', '{', '[', push it onto the stack.
4. If the character is a closing bracket ')', '}', ']':
    a. Check if the stack is empty. If it is, the string is invalid (no matching opening bracket).
    b. Pop the top element from the stack.
    c. Check if the popped element is the corresponding opening bracket. If not, the string is invalid.
5. After iterating through the entire string, check if the stack is empty.
    If it is empty, all opening brackets were matched and closed correctly -> Valid.
    If it is not empty, there are unmatched opening brackets -> Invalid.
"""


def isValid(s: str) -> bool:   
    ## initializing empty stack 
    stack = []

    for i in s: 
        if i == "(" or i == "[" or i == "{" : 
            stack.append(i)
        elif i == ")" or i == "]" or i == "}" :
            if stack is None:
                return False
            last_element = stack.pop()
            if last_element == "(" and i == ")" or last_element == "[" and i == "]" or last_element == "{" and i == "}" : 
                return True
            else: 
                return False
        else:
            return False
    if stack is None:
        return True 
    else:
        return False

### TODO: there is one more edge case to handle that is still giving me an error 

s = "]"

print(isValid(s))

    
