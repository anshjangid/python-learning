
# Take a 4 digit number as input and find the sum of its first two digits and the sum of its last two digits separately. Also, check if the two sums are equal or not.


n=int(input("Enter 4 digit number:"))
a=(n//1000)
b=(n//100)%10
c=(n//10)%10
d=n%10
Sum1=a+b
Sum2=c+d
if Sum1 == Sum2 :
   print("Sums are equal")
else:
    print("Sums are not equal")
