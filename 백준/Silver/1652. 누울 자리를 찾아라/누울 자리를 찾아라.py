n = int(input())
room = [input().strip() for _ in range(n)]

horizontal = 0
vertical = 0

# 가로 자리 계산
for row in room:
    empty = 0
    for char in row:
        if char == '.':
            empty += 1
        else:
            if empty >= 2:
                horizontal += 1
            empty = 0
    if empty >= 2:
        horizontal += 1

# 세로 자리 계산
for col in range(n):
    empty = 0
    for row in range(n):
        if room[row][col] == '.':
            empty += 1
        else:
            if empty >= 2:
                vertical += 1
            empty = 0
    if empty >= 2:
        vertical += 1

print(horizontal, vertical)
