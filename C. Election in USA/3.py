with open('input.txt') as inp:
    results = {}
    for line in inp.readlines():
        man, number = line.strip().split(' ')
        try:
            results[man] += int(number)
        except:
            results[man] = int(number)

for res in sorted(results.items(), key=lambda x: x[0]):
    print("{} {}".format(res[0], res[1]))
