n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")
else:
    count = 0

    print("Divisors are:")

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            count = count + 1

    print("Total number of divisors:", count)

    if count == 2:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")