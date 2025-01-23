import sys
input = sys.stdin.readline

k, l = map(int, input().split())  
d = {}
for i in range(l):
    s = input().strip()
    d[s] = i

for s, _ in sorted(d.items(), key=lambda x: x[1])[:k]:
    print(s)
