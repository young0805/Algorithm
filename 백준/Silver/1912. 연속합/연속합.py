n = int(input())  # 수열의 크기
arr = list(map(int, input().split()))  # 수열 입력

# 동적 계획법을 이용해 최대 연속 부분 합 계산
for idx in range(1, n):
    arr[idx] = max(arr[idx], arr[idx] + arr[idx - 1])  # 이전까지의 합을 더하는 방식으로 최적화

# 최대 연속 부분 합 출력
print(max(arr))
