import sys
input = sys.stdin.read

MOD = 1_000_000_009
MAX_N = 100_000

dp = [[0] * 4 for _ in range(MAX_N + 1)]
dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1

for i in range(4, MAX_N + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

t, *cases = map(int, input().split())
results = [sum(dp[n]) % MOD for n in cases]
print('\n'.join(map(str, results)))
