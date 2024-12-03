def sort(lista):
    lista.sort(key=lambda x: x[1])  # Correct index (1) and removed reverse
    return lista

data = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
print(sort(data))

lowest_grade = data[0][1]

second_lowest = None

for student in data:
    if student[1] > lowest_grade:
        second_lowest = student[1]
        break

second_lowest_student = 