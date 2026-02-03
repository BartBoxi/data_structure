def valid_paranthesis(s: str) -> bool:
    parentheses_map = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in s:
        if char in parentheses_map:
            stack.append(char)
        else:
            if stack and parentheses_map[stack[-1]] == char:
                stack.pop()
            else:
                return False
    return not stack


print(valid_paranthesis('()}]{{[[]]]]]]}}]'))