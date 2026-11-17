sentence = input("Enter a sentence: ")
unique_text = ""

for char in sentence:
    found = False
    for u_char in unique_text:
        if char == u_char:
            found = True
            break
    if not found:
        unique_text += char

print("String after removing duplicates:", unique_text)