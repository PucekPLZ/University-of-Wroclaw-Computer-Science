def assign_seats(v, m):
    quotients = []
    for i in range(len(v)):
        for j in range(1, m+1):
            quotients.append((v[i]/j, i))

    quotients.sort(key=lambda x: x[0], reverse=True)
    seats = [0] * len(v)

    for i in range(m):
        seats[quotients[i][1]] += 1

    return seats

def election_result(votes, mandates):
    M = []
    for i in range(len(votes)):
        M.append(assign_seats(votes[i], mandates[i]))

    results = [0, 0, 0, 0, 0]

    for i in M:
        for j in range(5):
            results[j] += i[j]

    return results