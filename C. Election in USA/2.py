f = open('input.txt')
results = f.readlines()
f.close()

people, votes = [], []

for result in results:
    result = result.strip().split()
    person, vote = result[0], result[1]
    try:
        idx = people.index(person)
        votes[idx] += vote
    except ValueError:
        people.append(person)
        votes.append(vote)

results = sorted(zip(people, votes), key=lambda x: x[0])
for result in results:
    print(result[0] + ' ' + str(result[1]))
