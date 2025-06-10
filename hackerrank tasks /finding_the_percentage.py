### this is the test code that used before submition of the main task

dict = {"adam":(10,12,13)}

name = str(input("what is your name"))

if name in dict:
    number_tuple = dict[name]

    if number_tuple:
        average = sum(number_tuple) / len(number_tuple)
        print(f"the average is: {average:.2f}")


### here is the code for the main task:

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        number_tuple = student_marks[query_name]

        if number_tuple:
            average = sum(number_tuple) / len(number_tuple)
            print(f"{average:.2f}")



