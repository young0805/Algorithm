T = int(input())  
test_cases = [int(input()) for _ in range(T)]  

max_n = max(test_cases)

# DP 배열 초기화 (P(1)부터 P(max_n)까지 계산할 수 있도록 크기 설정)
dp = [0] * (max_n + 1)

dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

# DP 점화식 계산 (P(n) = P(n-1) + P(n-5))
for i in range(6, max_n + 1):
    dp[i] = dp[i-1] + dp[i-5]

for n in test_cases:
    print(dp[n])
