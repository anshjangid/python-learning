sentence = input("Enter a sentence: ")
length = 0
total_chars = 0

for char in sentence:
    total_chars += 1

i = total_chars
while i > 0 and sentence[i - 1] == " ":
    i -= 1

while i > 0 and sentence[i - 1] != " ":
    length += 1
    i -= 1

print("Length of last word:", length)
