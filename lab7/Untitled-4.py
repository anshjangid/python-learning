text = input("Enter a string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for letter in alphabet:
    found = False
    for char in text:
        if char == letter or char == chr(ord(letter) - 32):
            found = True
            break
    if not found:
        is_pangram = False
        break

if is_pangram:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")