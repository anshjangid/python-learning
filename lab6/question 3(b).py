n = int(input("Enter the number of lines: "))

if n <= 0:
    print("Invalid input")
else:
    i = n

    while i >= 1:
        j = 1

        while j <= i:
            print("*", end=" ")
            j = j + 1

        print()
        i = i - 1