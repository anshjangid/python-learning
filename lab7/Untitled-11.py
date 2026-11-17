paragraph = input("Enter a paragraph: ")
digits = 0
alphas = 0
upper_case = 0
lower_case = 0
special_chars = 0

for char in paragraph:
    if "0" <= char <= "9":
        digits += 1
    elif "a" <= char <= "z":
        alphas += 1
        lower_case += 1
    elif "A" <= char <= "Z":
        alphas += 1
        upper_case += 1
    else:
        special_chars += 1

print("Digits count:", digits)
print("Total alphabets count:", alphas)
print("Upper case count:", upper_case)
print("Lower case count:", lower_case)
print("Special characters count:", special_chars)