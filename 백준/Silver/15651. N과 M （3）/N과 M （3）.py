def backtrack(n, m, path):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return

    for i in range(1, n + 1):
        backtrack(n, m, path + [i])

n, m = map(int, input().split())
backtrack(n, m, [])
