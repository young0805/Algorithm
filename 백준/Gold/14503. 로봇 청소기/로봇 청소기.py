n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1]

cleaned = 0

def turn_left(direction):
    return (direction + 3) % 4

while True:
    if room[x][y] == 0:
        room[x][y] = 2
        cleaned += 1

    moved = False
    for _ in range(4):
        d = turn_left(d)
        nx, ny = x + dx[d], y + dy[d]

        if room[nx][ny] == 0:
            x, y = nx, ny
            moved = True
            break

    if not moved:
        nx, ny = x - dx[d], y - dy[d]
        if room[nx][ny] == 1:
            break
        x, y = nx, ny

print(cleaned)
