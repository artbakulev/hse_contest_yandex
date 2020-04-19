n = int(input())
dictionary = {input() for i in range(n)}

s = input()
words = s.split(' ')
errors = 0
for word in words:
    if word in dictionary:
        continue

    uppers = 0
    for char in word:
        if char.isupper():
            uppers += 1

    if uppers == 0 or uppers > 1:
        errors += 1

print(errors)
