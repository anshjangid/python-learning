text = input("Enter text: ")
shift = int(input("Enter shift: "))
cipher_text = ""

for char in text:
    if "a" <= char <= "z":
        new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        cipher_text += new_char
    elif "A" <= char <= "Z":
        new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        cipher_text += new_char
    else:
        cipher_text += char

print("Encrypted text:", cipher_text)