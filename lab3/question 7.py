
#. Take a 3 digit number as input. Check if it is a Harshad number or not, i.e. whether the number is exactly divisible by the sum of its digits. E.g. 1 + 5 + 3 = 9 and 153 / 9 = 17, so 153 is a Harshad number.



n=int(input("Enter 3 digit number:"))
n>100 and n<999

n1=n//100
n2=(n//10)%100
n3=n%10
Sum=n1+n2+n3
if n%Sum == 0:
    print("It is a Harshad number")
else:
    print("It is not a Harshad number")


