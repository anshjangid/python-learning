text = input("Enter a string: ")
length = len(text)
is_palindrome = True

for i in range(length // 2):
    if text[i] != text[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")