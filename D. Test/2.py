def count_ups(s):
    total = 0
    for i in s:
        if i.isupper():
            total += 1
    return total


n = int(input())
udareniya = {}
for i in range(n):
    word = input()
    word_lower = word.lower()
    if word_lower not in udareniya:
        udareniya[word_lower] = set()
    udareniya[word_lower].add(word)

errors = 0
sentence = input().split()
for word in sentence:
    word_lower = word.lower()
    if (word_lower in udareniya and word not in udareniya[word_lower]
            or count_ups(word) != 1):
        errors += 1
print(errors)
