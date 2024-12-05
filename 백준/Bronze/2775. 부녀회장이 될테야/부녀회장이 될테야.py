t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    residents = [[] for _ in range(k + 1)]
    residents[0] = [i for i in range(1, n + 1)]

    for floor in range(1, k + 1):
        for room in range(n):
            residents[floor].append(sum(residents[floor - 1][0:room + 1]))

    print(residents[k][n - 1])
