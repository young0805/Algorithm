def find_winner(board):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # 가로, 세로, 두 대각선
    for x in range(19):
        for y in range(19):
            if board[x][y] == 0:
                continue
            color = board[x][y]
            for dx, dy in directions:
                nx, ny = x, y
                count = 0
                for _ in range(5):  # 다섯 칸 확인
                    if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                        count += 1
                        nx, ny = nx + dx, ny + dy
                    else:
                        break
                if count == 5:  # 여섯 번째 확인
                    if not (0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color) and \
                       not (0 <= x - dx < 19 and 0 <= y - dy < 19 and board[x - dx][y - dy] == color):
                        return color, x + 1, y + 1
    return 0, None, None


board = [list(map(int, input().split())) for _ in range(19)]

# 결과 확인
winner, row, col = find_winner(board)

if winner:
    print(winner)
    print(row, col)
else:
    print(0)
