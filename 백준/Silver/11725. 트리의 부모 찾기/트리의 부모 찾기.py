from collections import deque

def find_parents(n, edges):
    # 트리 구조를 인접 리스트로 표현
    adj = [[] for _ in range(n + 1)]
    
    # 주어진 간선 정보를 바탕으로 인접 리스트 채우기
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    parents = [-1] * (n + 1)
    
    # BFS를 위한 큐 초기화
    queue = deque([1])
    parents[1] = 0 
    
    # BFS 탐색
    while queue:
        current = queue.popleft()
        
        # 현재 노드와 연결된 다른 노드들을 탐색
        for neighbor in adj[current]:
            if parents[neighbor] == -1:  
                parents[neighbor] = current  
                queue.append(neighbor) 
    
    return parents[2:]

n = int(input())  
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# 부모 노드 구하기
parents = find_parents(n, edges)

# 결과 출력
print(*parents, sep='\n')
