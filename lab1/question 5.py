
#. Input two positive integers x and y. Check whether y is divisible by x. For negative inputs, display 'Invalid Input'. 



x = int(input("Enter first integer (x): "))
y = int(input("Enter second integer (y): "))

if x < 0 or y < 0:
    print("Invalid input")
else:
    if y % x == 0:
        print(f"{y} is divisible by {x}")
    else:
        print(f"{y} is not divisible by {x}")