txt = input().split()

voteCount = {}
winner = ""

for name in set(txt):
    voteCount[name] = txt.count(name)

for name, count in voteCount.items():
    if count == max(voteCount.values()):
        winner = name
    print(f"{name} : {count}")


print("Winner:", winner)
