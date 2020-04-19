dictionary = {input() for i in range(int(input()))}
s = input().split(' ')

errors = len(s)
for word in s:
    if word not in dictionary:
        uppers = 0
        for char in word:
            if char.isupper():
                uppers += 1
                if uppers > 1:
                    errors = errors - 1
print(errors)
