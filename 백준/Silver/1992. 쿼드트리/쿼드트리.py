def compress(x, y, size):
    initial = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != initial:
                half = size // 2
                return "(" + \
                       compress(x, y, half) + \
                       compress(x, y + half, half) + \
                       compress(x + half, y, half) + \
                       compress(x + half, y + half, half) + \
                       ")"
    return initial

n = int(input())
matrix = [input().strip() for _ in range(n)]

print(compress(0, 0, n))
