n = int(input())

lines = []
for i in range(n):
    lines.append(input())

s = input()
words = s.split(' ')
errors = 0
for word in words:
    if word not in lines:
        uppers = 0
        word.count()
        for char in word:
            if ord('A') <= ord(char) <= ord('Z'):
                uppers += 1

        if uppers != 1:
            errors += 1

print(errors)
