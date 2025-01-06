def find_winner(n, p):
    candidates = [0] * n
    bowl = p
    current = 0

    while True:
        if bowl > 0:
            candidates[current] += 1
            bowl -= 1
        else:
            bowl += candidates[current]
            candidates[current] = 0

        if bowl == 0 and sum(candidates) == candidates[current]:
            return current

        current = (current + 1) % n

results = []
while True:
    n, p = map(int, input().split())
    if n == 0 and p == 0:
        break
    results.append(find_winner(n, p))

for result in results:
    print(result)