n, m = map(int, input().split())
graph = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_sum = float('inf')
result = 0

for i in range(n):
    total = sum(graph[i])
    if total < min_sum:
        min_sum = total
        result = i + 1

print(result)
