with open('input.txt') as f:
    results = {}
    for line in f.readlines():
        person, votes = line.strip().split(' ')
        try:
            results[person] += int(votes)
        except KeyError:
            results[person] = int(votes)

[print(_[0] + ' ' + str(_[1])) for _ in
 sorted(results.items(), key=lambda x: x[0])]
