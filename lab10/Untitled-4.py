txt = input()
dict = {}

for ch in txt:
    if ch not in dict:
        dict[ch] = txt.count(ch)

print(dict)
