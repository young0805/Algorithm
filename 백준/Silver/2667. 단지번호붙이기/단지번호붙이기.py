def solve_complex_numbering():
    import sys
    input = sys.stdin.read

    # DFS 함수 정의 (스택 사용)
    def dfs(x, y):
        stack = [(x, y)]
        count = 0

        while stack:
            cx, cy = stack.pop()
            if 0 <= cx < N and 0 <= cy < N and grid[cy][cx] == 1:
                grid[cy][cx] = 0 
                count += 1
                # 상하좌우 이동
                for dx, dy in directions:
                    stack.append((cx + dx, cy + dy))

        return count

    data = input().splitlines()
    N = int(data[0])  # 지도의 크기
    grid = [list(map(int, line)) for line in data[1:]]  # 지도 정보

    # 상하좌우 탐색을 위한 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    complexes = []  # 각 단지의 집의 수를 저장할 리스트

    # 지도 탐색
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1: 
                house_count = dfs(x, y)
                complexes.append(house_count)

    complexes.sort()  # 단지별 집의 수를 오름차순 정렬
    print(len(complexes))  # 총 단지 수 출력
    print("\n".join(map(str, complexes)))  # 각 단지의 집의 수 출력

# 함수 실행
if __name__ == "__main__":
    solve_complex_numbering()
