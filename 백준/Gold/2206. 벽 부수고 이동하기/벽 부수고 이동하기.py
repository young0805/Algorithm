from collections import deque

def shortest_path_with_wall_break(n, m, grid):
    move_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, wall_broken = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][wall_broken]

        for dx, dy in move_directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 0 and visited[nx][ny][wall_broken] == 0:
                    visited[nx][ny][wall_broken] = visited[x][y][wall_broken] + 1
                    queue.append((nx, ny, wall_broken))

                if grid[nx][ny] == 1 and wall_broken == 0:
                    visited[nx][ny][1] = visited[x][y][wall_broken] + 1
                    queue.append((nx, ny, 1))

    return -1

try:
    n, m = map(int, input().split())
    grid = [list(map(int, input().strip())) for _ in range(n)]
    print(shortest_path_with_wall_break(n, m, grid))

except ValueError as e:
    print("입력 오류:", e)
except Exception as e:
    print("예기치 못한 오류:", e)
