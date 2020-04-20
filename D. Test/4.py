n = int(input())

lines = []
lines_small = []
for i in range(n):
    word = input()
    lines.append(word)
    lines_small.append(word.lower())

s = input()
words = s.split(' ')
errors = 0
for word in words:
    if word not in lines:
        if word.lower() in lines_small:
            errors += 1
        else:
            uppers = 0
            for char in word:
                if ord('A') <= ord(char) <= ord('Z'):
                    uppers += 1

            if uppers != 1:
                errors += 1

print(errors)
