from collections import defaultdict, deque

def topological_sort(N, comparisons):
    
    # 1. 그래프와 진입 차수 초기화
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    
    # 2. 주어진 비교 결과로 그래프 생성
    for A, B in comparisons:
        graph[A].append(B)
        in_degree[B] += 1
    
    # 3. 진입 차수가 0인 노드들을 큐에 추가
    queue = deque(i for i in range(1, N + 1) if in_degree[i] == 0)
    
    # 4. 위상 정렬 수행
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1  
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

N, M = map(int, input().split())
comparisons = [tuple(map(int, input().split())) for _ in range(M)]

result = topological_sort(N, comparisons)
print(" ".join(map(str, result)))
