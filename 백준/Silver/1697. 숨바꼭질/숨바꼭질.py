from collections import deque

def find_fastest_time(N, K):
    MAX = 100000
    visited = [-1] * (MAX + 1)

    # BFS를 위한 큐 초기화
    queue = deque([N])
    visited[N] = 0  

    while queue:
        current = queue.popleft()

        # 현재 위치가 동생의 위치인 경우 시간 반환
        if current == K:
            return visited[current]

        # 이동 가능한 경우 탐색: 왼쪽으로 걷기, 오른쪽으로 걷기, 순간이동
        for next_pos in (current - 1, current + 1, current * 2):
            # 이동 가능한 범위 내이고 아직 방문하지 않은 경우
            if 0 <= next_pos <= MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# 수빈이의 위치(N)와 동생의 위치(K) 입력 받기
N, K = map(int, input().split())

print(find_fastest_time(N, K))
