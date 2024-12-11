import sys

num_elements = int(sys.stdin.readline())  # 수열의 크기 입력
sequence = list(map(int, sys.stdin.readline().split()))  # 수열 입력
longest_increasing_subsequence = [1] * num_elements  # 가장 긴 증가하는 부분 수열의 길이를 저장할 배열

# 동적 계획법을 사용하여 가장 긴 증가하는 부분 수열 길이 계산
for current_index in range(1, num_elements):
    for previous_index in range(current_index):
        if sequence[current_index] > sequence[previous_index]:
            longest_increasing_subsequence[current_index] = max(longest_increasing_subsequence[current_index], longest_increasing_subsequence[previous_index] + 1)

# 가장 긴 증가하는 부분 수열의 길이 출력
print(max(longest_increasing_subsequence))
