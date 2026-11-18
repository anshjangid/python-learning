inv = {}

def sell(item, quantity):
    inv[item] -= quantity

def add(item, quantity):
    if item in inv:
        inv[item] += quantity
    else:
        inv[item] = quantity

nItems = int(input())

for i in range(nItems):
    item, quantity = input().split()
    inv[item] = int(quantity)

n = int(input())

for i in range(n):
    choice, item, quantity = input().split()
    if choice == 'SELL':
        if int(quantity) > inv[item]:
            print('Insufficient stock:', item)
        else:
            sell(item, int(quantity))
    elif choice == 'ADD':
        add(item, int(quantity))

for item, quantity in inv.items():
    print(item, quantity)
