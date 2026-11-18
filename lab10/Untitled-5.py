def simple_interest(p, r, t=1):
    return (p*r*t)/100

p = int(input())
r = int(input())

print(simple_interest(p, r))
print(simple_interest(p, r, 3))
