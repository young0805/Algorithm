def backtrack(n, m, start, path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(start, n + 1):
        backtrack(n, m, i + 1, path + [i])

n, m = map(int, input().split())
backtrack(n, m, 1, [])
