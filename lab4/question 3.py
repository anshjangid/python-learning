

shape = input("Shape: ")





if shape == "square":
    s = float(input("Side: "))
    print(s * s)

elif shape == "rectangle":
    l = float(input("Length: "))
    w = float(input("Width: "))
    print(l * w)

elif shape == "circle":
    r = float(input("Radius: "))
    print(3.14 * r * r)

elif shape == "triangle":
    b = float(input("Base: "))
    h = float(input("Height: "))
    print(0.5 * b * h)

else:
    print("Wrong shape")
