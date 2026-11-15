
#. Take 3 angles as input, and find whether they can form the angles of a triangle or not. If they can, further classify the triangle as acute-angled, right-angled or obtuse-angled. Consider invalid cases also.


a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid angles. Angles must be positive.")
elif a + b + c != 180:
    print("Invalid angles. Sum must be 180°.")
else:
    if a < 90 and b < 90 and c < 90:
        print("The triangle is Acute-angled.")
    elif a == 90 or b == 90 or c == 90:
        print("The triangle is Right-angled.")
    else:
        print("The triangle is Obtuse-angled.")
        