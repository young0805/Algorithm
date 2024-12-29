import math

def calculate_bridges(test_cases):
    results = []
    for n, m in test_cases:
        # 조합을 계산: mCn
        results.append(math.comb(m, n))
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]

results = calculate_bridges(test_cases)

for result in results:
    print(result)
