from itertools import combinations

def count_cake_combinations(n, cake_sizes):
    cake_fractions = [1 / c for c in cake_sizes]
    count = 0
    for r in range(1, n + 1):
        for subset in combinations(cake_fractions, r):
            total = sum(subset)
            if 0.99 <= total <= 1.01:
                count += 1
    return count

n = int(input())
cake_sizes = list(map(int, input().split()))
print(count_cake_combinations(n, cake_sizes))
