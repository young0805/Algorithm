import sys
input = sys.stdin.readline

n = int(input())
tips = sorted([int(input()) for _ in range(n)], reverse=True)
print(sum(max(0, tips[i] - i) for i in range(n)))
