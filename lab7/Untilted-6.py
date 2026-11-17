counts = [0, 0, 0, 0, 0]
total = 0

while True:
    val = int(input("Enter number (1-10) or -1 to stop: "))
    if val == -1:
        break
    if 1 <= val <= 10:
        total += 1
        if val == 1 or val == 2:
            counts[0] += 1
        elif val == 3 or val == 4:
            counts[1] += 1
        elif val == 5 or val == 6:
            counts[2] += 1
        elif val == 7 or val == 8:
            counts[3] += 1
        elif val == 9 or val == 10:
            counts[4] += 1

ranges = ["1-2 ", "3-4 ", "5-6 ", "7-8 ", "9-10"]
for i in range(5):
    pct = (counts[i] / total * 100) if total > 0 else 0.0
    stars = ""
    for _ in range(counts[i]):
        stars += "#"
    print(f"{ranges[i]}: {stars} {pct:.2f} %")