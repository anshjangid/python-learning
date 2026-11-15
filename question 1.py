
# Write a program that prompts the user to enter the centre of a circle (x1, y1), its radius r, and a second point (x2, y2), and displays whether the second point lieinside, on the boundary of, or outside the circle. The formula for computing the distance between two points is distance = √[(x2 – x1)2 + (y2 – y1)2]



x1 = float(input("Enter x-coordinate of circle center: "))
y1 = float(input("Enter y-coordinate of circle center: "))
r = float(input("Enter radius of the circle: "))

x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

if distance < r:
    print("The point lies inside the circle.")
elif distance == r:
    print("The point lies on the boundary of the circle.")
else:
    print("The point lies outside the circle.")