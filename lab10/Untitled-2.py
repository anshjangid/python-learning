def count_vowels(txt):
    count = 0
    for ch in txt:
        if ch in 'aeiou':
            count += 1
    return count

txt = input().lower()
print('Vowels:',count_vowels(txt))
