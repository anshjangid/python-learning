num = int(input("Enter a positive integer: "))
d = int(input("Enter a digit (0-9): "))

if num <= 0 or d < 0 or d > 9:
    print("Invalid input")
else:
    count = 0
    temp = num

    while temp > 0:
        digit = temp % 10

        if digit == d:
            count = count + 1

        temp = temp // 10

    print("Digit occurs", count, "times")