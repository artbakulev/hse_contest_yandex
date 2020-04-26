n, accents = int(input()), dict()

for _ in range(n):
    word = input();
    low = word.lower()
    if low not in accents:
        accents[low] = set()
    accents[low].add(word)

total_errors = 0


def counter(s):
    return sum(map(str.isupper, s))


sentence = input().split()
for word in sentence:
    low = word.lower()
    if low in accents and word not in accents[low]:
        total_errors = total_errors + 1
    elif counter(word) != 1:
        total_errors = total_errors + 1
print(total_errors)
