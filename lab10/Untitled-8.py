n = int(input())
dic = {}

for i in range(n):
    country, capital = input().split()
    dic[country] = capital

query = input()

if query in dic:
    print(dic[query])
else:
    print("Not found")
