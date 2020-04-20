def upper_count(s):
    ups = filter(lambda x: x.isupper(), s)
    return len(list(ups))


n = int(input())
lines = {input() for i in range(n)}
linesLower = {line.lower() for line in lines}

words, number_of_errors = input().split(' '), 0

for word in words:
    count = upper_count(word)
    if (word not in lines and word.lower() in linesLower) or count != 1:
        number_of_errors += 1
print(number_of_errors)
