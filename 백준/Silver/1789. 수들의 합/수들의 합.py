S = int(input())  # 합 S 입력
current_sum = 0   # 현재 합산된 값
max_count = 0     # 자연수 N의 개수

for num in range(1, S + 1):  # 1부터 S까지 자연수를 반복
    current_sum += num       # 현재 합산 값에 num 추가
    max_count += 1           # 자연수 개수 증가
    if current_sum > S:      # 합이 S를 초과하면
        max_count -= 1       # 초과한 경우 개수를 감소
        break

print(max_count)  # 최대 자연수 N 출력
