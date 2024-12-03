grades = [20, 40, 43, 57, 89]

def grading(grades):
    grades_results = []
    for i in grades:
        if i < 40:
            grades_results.append(i)
        elif i >= 40 and i % 5 == 0:
            grades_results.append(i)
        elif i >= 40 and i % 5 != 0:
            a = round(i / 5)
            b = (a * 5) - i
            print(b)
            if b <= 3 and b > 0:
                i = (a * 5)
                grades_results.append(i)
            else:
                grades_results.append(i)
    print(grades_results)


grading(grades)



# a = 84
# b = round(a / 5)
# c = (b * 5) - a
# print(a,b,c)
