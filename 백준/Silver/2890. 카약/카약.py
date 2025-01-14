r, c = map(int, input().split())
x = []
result = []
rank = 1
result_team = []

for _ in range(r):
    x.append(list(input()))

for i in range(r):
    cnt = 0
    for j in range(c):
        if x[i][j] not in {"S", ".", "F"}:
            del x[i][j]
            cnt += 1
        if cnt == 2:
            break

check = [len(i) for i in x]
for i in range(len(check)):
    if check[i] == max(check):
        delete = i
del x[delete]

for i in range(1, c - 1):
    cnt = 0
    for j in range(r - 1):
        if x[j][-i] not in {"F", ".", "S"}:
            result.append(rank)
            result_team.append(int(x[j][-i]))
            cnt += 1
    if cnt > 0:
        rank += 1

for i in range(1, 10):
    print(result[result_team.index(i)])
