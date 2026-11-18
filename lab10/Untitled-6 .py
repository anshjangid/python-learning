def  get_grade(marks):
    if marks >= 80:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 40:
        return 'C'
    else:
        return 'F'

n = int(input())
dict = {}

for i in range(n):
    student = input().split()
    dict[student[0]] = get_grade(int(student[1]))

for name, grade in dict.items():
    print(f"{name}: {grade}")

gradeCount = {}

for grade in dict.values():
    if grade in gradeCount:
        gradeCount[grade] += 1
    else:
        gradeCount[grade] = 1

print(gradeCount)
