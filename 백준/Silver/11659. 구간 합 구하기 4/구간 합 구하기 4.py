import sys
input = sys.stdin.read
data = input().split()

n, m = map(int, data[:2])
arr = list(map(int, data[2:n+2]))
queries = data[n+2:]

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

results = []
for k in range(m):
    i, j = map(int, queries[k * 2:k * 2 + 2])
    results.append(prefix[j] - prefix[i - 1])

sys.stdout.write("\n".join(map(str, results)) + "\n")
