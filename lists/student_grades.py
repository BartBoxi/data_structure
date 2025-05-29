if __name__ == '__main__':
    records = []
    try:
        n = int(input("Enter number of students: "))
        for _ in range(n):
            name = input("Enter name: ")
            score = float(input("Enter score: "))
            records.append([name, score])
    except ValueError as e:
        print("Invalid input! Please enter numbers where expected.")

    highest_score = float('-inf')
    top_student = ''

    for name, score in records:
        if score > highest_score:
            highest_score = score
            top_student = name
    print(top_student)

### correct answer

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    unique_scores = sorted(set(score for _, score in records))
    second_lowest = unique_scores[1]

    names_with_second = sorted(name for name, score in records if score == second_lowest)

    for name in names_with_second:
        print(name)





