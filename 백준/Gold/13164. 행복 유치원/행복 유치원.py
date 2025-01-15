n, k = map(int, input().split())
heights = list(map(int, input().split()))

diffs = [heights[i + 1] - heights[i] for i in range(n - 1)]
diffs.sort()

print(sum(diffs[:n - k]))
