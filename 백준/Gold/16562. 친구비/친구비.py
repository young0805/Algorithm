import sys
input = sys.stdin.read

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if cost[root_x] < cost[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y

data = input().split()
N, M, k = map(int, data[:3])
cost = [0] + list(map(int, data[3:3+N]))
parent = list(range(N + 1))

edges = data[3+N:]
for i in range(0, len(edges), 2):
    v, w = map(int, edges[i:i+2])
    union(v, w)

total_cost = 0
unique_groups = set(find(i) for i in range(1, N + 1))
for group in unique_groups:
    total_cost += cost[group]

print(total_cost if total_cost <= k else "Oh no")
