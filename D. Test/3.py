n = int(input())
dictionary = {input() for i in range(n)}
small_dictionary = set()

for word in dictionary:
    small_dictionary.add(word.lower())

s = input()
words = s.split(' ')
errors = 0
for word in words:
    if word in dictionary:
        continue

    if word in small_dictionary:
        errors += 1
        continue

    uppers = 0
    for char in word:
        if char.isupper():
            uppers += 1

    if uppers == 0 or uppers > 1:
        errors += 1

print(errors)
