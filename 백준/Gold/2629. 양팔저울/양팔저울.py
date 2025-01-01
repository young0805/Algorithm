n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

possible = set([0])

for weight in weights:
    current = list(possible)
    for p in current:
        possible.add(p + weight)
        possible.add(abs(p - weight))

result = []
for marble in marbles:
    if marble in possible:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(result))
