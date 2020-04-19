s = input()
for i, c in enumerate(s):
    if i % 3 == 0:
        continue
    print(c, end='')
