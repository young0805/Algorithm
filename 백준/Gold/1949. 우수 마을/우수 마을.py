import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.read

def dfs(node, parent):
    dp[node][0] = 0
    dp[node][1] = population[node - 1]
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            dp[node][0] += max(dp[neighbor][0], dp[neighbor][1])
            dp[node][1] += dp[neighbor][0]

data = input().split()
N = int(data[0])
population = list(map(int, data[1:N + 1]))
edges = data[N + 1:]

tree = defaultdict(list)
for i in range(0, len(edges), 2):
    a, b = int(edges[i]), int(edges[i + 1])
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]
dfs(1, -1)
print(max(dp[1][0], dp[1][1]))
