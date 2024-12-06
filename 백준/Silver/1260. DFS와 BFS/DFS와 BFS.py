N, M, start_vertex = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(vertex):
    visited_dfs[vertex] = True
    print(vertex, end=' ')
    for i in range(1, N + 1):
        if graph[vertex][i] == 1 and not visited_dfs[i]:
            dfs(i)

def bfs(start_vertex):
    queue = [start_vertex]
    visited_bfs[start_vertex] = True
    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for i in range(1, N + 1):
            if graph[vertex][i] == 1 and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(start_vertex)
print()
bfs(start_vertex)
