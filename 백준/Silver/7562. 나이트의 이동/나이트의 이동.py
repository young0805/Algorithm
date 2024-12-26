from collections import deque

# 나이트의 8방향 이동 (체스판에서 나이트가 이동할 수 있는 8가지 방향)
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs(l, start, target):
    # 시작 위치와 목표 위치가 같으면 0번 이동
    if start == target:
        return 0

    # 방문 처리 배열
    visited = [[False] * l for _ in range(l)]
    
    # 큐 초기화: (x, y, 이동 횟수)
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    
    # BFS 탐색
    while queue:
        x, y, dist = queue.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if (nx, ny) == target:
                    return dist + 1
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1

def main():
    t = int(input())  
    for _ in range(t):
        l = int(input()) 
        start = tuple(map(int, input().split()))  
        target = tuple(map(int, input().split())) 
        
        print(bfs(l, start, target))

if __name__ == "__main__":
    main()
