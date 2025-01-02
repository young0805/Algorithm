import sys
input = sys.stdin.read

data = input().splitlines()
board = [list(map(int, line.split())) for line in data[:10]]

sheets = [0] + [5] * 5
min_count = float('inf')

# 특정 크기의 색종이를 특정 위치에 놓을 수 있는지 확인
def can_cover(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if board[x + i][y + j] == 0:
                return False
    return True

# 색종이를 놓거나 되돌리는 함수
def cover(x, y, size, state):
    for i in range(size):
        for j in range(size):
            board[x + i][y + j] = state

# 재귀적으로 색종이 붙이기
def dfs(count):
    global min_count

    # 모든 칸이 덮였으면 최소값 갱신
    if all(board[i][j] == 0 for i in range(10) for j in range(10)):
        min_count = min(min_count, count)
        return

    # 남은 최소값보다 더 많은 색종이를 쓰는 경우
    if count >= min_count:
        return

    # 색종이를 놓을 위치 찾기
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                # 1x1부터 5x5까지 시도
                for size in range(1, 6):
                    if sheets[size] > 0 and can_cover(i, j, size):
                        cover(i, j, size, 0)
                        sheets[size] -= 1
                        dfs(count + 1)
                        cover(i, j, size, 1)
                        sheets[size] += 1
                return

# DFS 시작
dfs(0)

print(min_count if min_count != float('inf') else -1)
