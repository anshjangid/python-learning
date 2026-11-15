n = int(input("Enter the number of integers: "))

total = 0

for i in range(1, n + 1):
    num = int(input(f"Enter integer {i}: "))
    total += num

print("The sum of integers is:", total)