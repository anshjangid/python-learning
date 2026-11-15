num = int(input("Enter an integer: "))

if num <= 0:
    print("Invalid input")
else:
    total = 0

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total = total + i

    if total == num:
        print(num, "is a perfect number")
    else:
        print(num, "is not a perfect number")