def sorter(a):
    return a[0]


with open('input.txt') as f:
    lines = f.readlines()

candidates, results = [], []

for line in lines:
    candidate, votes = line.strip().split(' ')
    votes = int(votes)
    if candidate in candidates:
        idx = -1
        for i in range(len(candidates)):
            if candidate == candidates[i]:
                idx = i
        results[idx] += votes
    else:
        candidates.append(candidate)
        results.append(votes)

general = []
for i in range(len(candidates)):
    general.append((candidates[i], results[i]))

general.sort(key=sorter)

for result in general:
    print(result[0] + ' ' + str(result[1]))
