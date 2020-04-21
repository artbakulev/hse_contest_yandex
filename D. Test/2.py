dictionary = {input() for i in range(int(input()))}
dictionary_lower = {word.lower() for word in dictionary}
s = input().split(' ')

errors = 0
for word in s:
    if word not in dictionary:
        if word.lower() in dictionary_lower:
            errors += 1
        else:
            uppers = 0
            for char in word:
                if char.isupper():
                    uppers += 1
            if uppers != 1:
                errors += 1
print(errors)
