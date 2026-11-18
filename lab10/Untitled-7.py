tup = tuple(map(int, input().split()))
evenTup = ()

for i in tup:
    if i % 2 == 0:
        evenTup += (i,)

print(evenTup)
