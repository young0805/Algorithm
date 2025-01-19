k = int(input())
for i in range(1, k + 1):
    data = list(map(int, input().split()))
    n = data[0]
    scores = sorted(data[1:], reverse=True)
    max_score = scores[0]
    min_score = scores[-1]
    max_gap = 0

    for j in range(n - 1):
        gap = scores[j] - scores[j + 1]
        if gap > max_gap:
            max_gap = gap

    print(f"Class {i}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {max_gap}")
