txt = input().split()
v = int(input())
tup = tuple(map(int,txt))

print('Tuple:',tup)
print('Length:',len(tup))
print(f'Count of {v}:',tup.count(v))
print(f'First index of {v}:',tup.index(v))
