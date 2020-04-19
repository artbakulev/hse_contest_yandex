f = open('input.txt')
results = f.readlines()
f.close()

people = []
votes = []

for result in results:
    result = result.strip()
    person = result.split(' ')[0]
    vote = int(result.split(' ')[1])

    if person in people:
        idx = people.index(person)
        votes[idx] += vote
    else:
        people.append(person)
        votes.append(vote)

results = sorted(zip(people, votes), key=lambda x: x[0])
for result in results:
    print(result[0] + ' ' + str(result[1]))
