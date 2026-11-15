
#Write a program that prompts the user to enter the side of a regular pentagon and displays its area. The formula for computing the area of a pentagon is Area = (5 * s2) / (4 * tan(π / 5)), where s is the length of a side


s = float(input("Enter the side length of the pentagon: "))
import math
area = (5 * (s**2)) / (4 * math.tan(3.14 / 5))

print("The area of the pentagon is:", area)
