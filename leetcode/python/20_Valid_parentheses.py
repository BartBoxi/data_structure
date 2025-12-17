def isValid(s:str) -> bool:
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[': 
            stack.append(i)
        elif i == ')' or i == '}' or i == ']':
            if not stack:
                return False
            last_element = stack.pop()
            if last_element == "(" and i != ')': return False
            if last_element == "{" and i != '}': return False
            if last_element == "[" and i != ']': return False
        else:
            return False
    return len(stack) == 0
### testing part 

print(f"Test '()': {isValid('()')}")
print(f"Test '[': {isValid('[')}")
print(f"Test '[': {isValid('(')}")
print(f"Test '[': {isValid('(]')}")
print(f"Test '[': {isValid(']')}")



