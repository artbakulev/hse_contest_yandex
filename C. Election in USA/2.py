with open('input.txt') as f:
    lines, results = f.readlines(), {}

for line in lines:
    person, votes = line.strip().split(' ')
    if results.get(person) is not None:
        results[person] += int(votes)
    else:
        results[person] = int(votes)

results = sorted(list(results.items()), key=lambda x: x[0])
for result in results:
    print("{} {}".format(result[0], result[1]))
