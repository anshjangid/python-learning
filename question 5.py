
# Take a 5 digit number as input and print the largest digit of the number. Do not use any in-built functions and do not use loops. Also print the position of that digit counted from the left. If the largest digit occurs more than once, print the position of its first occurrence.



num = int(input('Enter a 5 digit number: '))
d1 = num // 10000
d2 = (num // 1000) % 10
d3 = (num // 100) % 10
d4 = (num // 10) % 10
d5 = num % 10
lar = d1
ct = 1
if lar < d2:
    ct = 2
    lar = d2
if lar < d3:
    ct = 3
    lar = d3
if lar < d4:
    ct = 4
    lar = d4
if lar < d5:
    ct = 5
    lar = d5
print('Largest digit is', lar, 'occurring at', ct, 'place')