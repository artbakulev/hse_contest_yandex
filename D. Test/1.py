def upper_count(s):
    ups = filter(lambda x: x.isupper(), s)
    return len(list(ups))


n = int(input())
accents = {}
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in accents:
        accents[base_form] = set()
    accents[base_form].add(word)

errors = 0
sentence = input().split()
for word in sentence:
    base_form = word.lower()
    if (base_form in accents and word not in accents[base_form]
            or upper_count(word) != 1):
        errors += 1
print(errors)
