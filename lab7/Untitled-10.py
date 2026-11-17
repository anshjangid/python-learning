raw_input = input("Enter hyphen-separated words: ")
words = []
current_word = ""

for char in raw_input:
    if char == "-":
        if current_word != "":
            words += [current_word]
            current_word = ""
    else:
        current_word += char
if current_word != "":
    words += [current_word]

num_words = len(words)
for i in range(num_words):
    for j in range(0, num_words - i - 1):
        if words[j] > words[j + 1]:
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp

result = ""
for i in range(num_words):
    if i == num_words - 1:
        result += words[i]
    else:
        result += words[i] + "-"

print("Sorted sequence:", result)