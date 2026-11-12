
# Input the radius of a circle (1–100 only) and calculate its area. Handle invalid inputs. 




r=float(input("radius of the circle (1-100):"))
area=3.14*r**2
if r >= 1 and r <= 100 :
   print(area)
else:
    print("check the value of the radius")