num_stairs = int(input())  # 계단의 개수 입력

# 계단의 점수를 저장할 배열
scores = [int(input()) for _ in range(num_stairs)]  

# 각 계단까지의 최댓값을 저장할 dp 배열
max_scores = [0] * num_stairs  

# 초기 조건 설정
if num_stairs > 0:
    max_scores[0] = scores[0]
if num_stairs > 1:
    max_scores[1] = scores[0] + scores[1]
if num_stairs > 2:
    max_scores[2] = max(scores[1] + scores[2], scores[0] + scores[2])

# 동적 계획법을 사용하여 각 계단까지의 최대 점수 계산
for i in range(3, num_stairs):
    max_scores[i] = max(max_scores[i-3] + scores[i-1] + scores[i], max_scores[i-2] + scores[i])

# 마지막 계단까지의 최댓값 출력
print(max_scores[num_stairs - 1])
