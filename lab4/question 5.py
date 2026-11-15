
n = float(input("Kilometers: "))
period = input("Day or night: ").lower()

# Taxi
if period == "day":
    taxi = 33.58 + 37.89*n
else:
    taxi = 33.58 + 43.17*n

# Bus
if n >= 20:
    bus = 4.32*n
else:
    bus = float('inf')   # not possible

# Train
if n >= 100:
    train = 2.88*n
else:
    train = float('inf') # not possible

# find cheapest
cheapest = taxi
name = "Taxi"

if bus < cheapest:
    cheapest = bus
    name = "Bus"

if train < cheapest:
    cheapest = train
    name = "Train"

print("Cheapest:", name, "=", round(cheapest,2), "INR")

