def solve_cabbage_problem():
    import sys
    from collections import deque  # BFS 사용
    
    input = sys.stdin.read

    # BFS 함수 정의
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        while queue:
            cx, cy = queue.popleft()
            if 0 <= cx < M and 0 <= cy < N and field[cy][cx] == 1:
                field[cy][cx] = 0  
                
                # 상하좌우 이동
                queue.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])

    data = input().splitlines()
    T = int(data[0])  

    results = []

    line_index = 1
    for _ in range(T):
        M, N, K = map(int, data[line_index].split())  
        line_index += 1

        field = [[0] * M for _ in range(N)]

        for _ in range(K):
            x, y = map(int, data[line_index].split())
            field[y][x] = 1
            line_index += 1

        worm_count = 0

        # 배추밭을 순회하며 BFS로 군집 탐색
        for y in range(N):
            for x in range(M):
                if field[y][x] == 1:  # 배추가 있는 경우
                    bfs(x, y)
                    worm_count += 1

        results.append(worm_count)

    print("\n".join(map(str, results)))

if __name__ == "__main__":
    solve_cabbage_problem()
