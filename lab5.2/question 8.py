n=input("Enter sentence")
capital=0
small=0
digit=0
special=0
for i in str(n):
    if "A"<=i<="Z":
        capital+=1
    elif "a"<=i<="z":
        small+=1
    elif '0'<i<'9':
        digit+=1
    else:
        special+=1
print(capital,small,digit,special)