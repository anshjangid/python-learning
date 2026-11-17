sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

word_len = 0
for c in word:
    word_len += 1

sent_len = 0
for c in sentence:
    sent_len += 1

count = 0
for i in range(sent_len - word_len + 1):
    match = True
    for j in range(word_len):
        if sentence[i + j] != word[j]:
            match = False
            break
    if match:
        count += 1

if count > 0:
    print("The sentence contains the word.")
else:
    print("The sentence does not contain the word.")
print("Occurrences:", count)