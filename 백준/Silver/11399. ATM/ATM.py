n = int(input())  # 사람 수
arr = list(map(int, input().split()))  # 각 사람이 돈을 인출하는 데 걸리는 시간

arr.sort()  # 시간 순으로 정렬
result = 0  # 총 대기 시간의 합
time = 0  # 현재까지의 대기 시간

# 각 사람의 대기 시간을 누적해서 더하기
for i in range(n):
    time += arr[i]  # 현재 사람의 인출 시간을 더함
    result += time  # 현재까지의 대기 시간을 합산

print(result)
