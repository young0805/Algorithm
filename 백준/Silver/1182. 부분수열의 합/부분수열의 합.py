def count_subsequences(num_count, target_sum, sequence):
    subsequence_count = 0
    # 1 << num_count는 2^num_count, 즉 부분수열의 개수
    for mask in range(1, 1 << num_count):  # 0은 공집합이므로 1부터 시작
        current_sum = 0
        for i in range(num_count):
            if mask & (1 << i):  # 비트가 1이면 해당 원소를 포함
                current_sum += sequence[i]
        if current_sum == target_sum:
            subsequence_count += 1
    return subsequence_count

# 입력 받기
num_count, target_sum = map(int, input().split())
sequence = list(map(int, input().split()))

result = count_subsequences(num_count, target_sum, sequence)
print(result)
