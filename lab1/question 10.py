total_classes = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))

percentage = (attended / total_classes) * 100

print("Attendance percentage =", percentage)

if percentage >= 75:
    print("Eligible for exams")
else:
    print("Not eligible for exams")