### list of strings operations where operations[i] is the ith opearon 
# x - record a new score
# + - record a new score equal to the sum of the previous two scores
# D - record a new score equal to the double of the previous score
# C - invalidate the previous score
# return the sum of all the scores


def calPoints(operations: list[str]) -> int:
    stack = []
    for operation in operations:
        if operation == "+":
            if len(stack) >= 2: ### in theory in the task it is written that it won't be an edge case but good to remember about it
                stack.append(stack[-1] + stack[-2])
            else:
                return -1
        elif operation == "D":
            stack.append(stack[-1]* 2)
        elif operation == "C":
            stack.pop()
        else:
            stack.append(int(operation))
    return sum(stack)


ops = ["5","2","C","D","+"]

print(calPoints(ops))

ops1 = ["5","-2","4","C","D","9","+","+"]

print(calPoints(ops1))

