n = int(input())
udar = {}
for i in range(n):
    word = input()
    base_form = word.lower()
    if base_form not in udar:
        udar[base_form] = set()
    udar[base_form].add(word)

counter = 0


def count_big(s):
    return sum(map(str.isupper, s))


sentence = input().split()
for word in sentence:
    base_form = word.lower()
    if (base_form in udar and word not in udar[base_form]
            or count_big(word) != 1):
        counter += 1
print(counter)
