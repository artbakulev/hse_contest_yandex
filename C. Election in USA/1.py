with open('input.txt') as f:
    lines = f.readlines()

results = {}
for line in lines:
    person, votes = line.strip().split(' ')
    try:
        results[person] += int(votes)
    except KeyError:
        results[person] = int(votes)

results = sorted(list(results.items()), key=lambda x: x[0])
for result in results:
    print(result[0] + ' ' + str(result[1]))
