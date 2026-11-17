raw_input = input("Enter numbers separated by spaces: ")
numbers = []
current = ""

for char in raw_input:
    if char == " ":
        if current != "":
            numbers += [int(current)]
            current = ""
    else:
        current += char
if current != "":
    numbers += [int(current)]

n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] < numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted list (descending):", numbers)