def calculate_score(scores):
    # 점수와 문제 번호를 묶어서 리스트로 저장
    indexed_scores = [(scores[i], i + 1) for i in range(len(scores))]
    
    indexed_scores.sort(reverse=True, key=lambda x: x[0])
    top_scores = indexed_scores[:5]
    
    total_score = sum(score for score, _ in top_scores)
    
    # 상위 점수에 해당하는 문제 번호를 오름차순 정렬
    problem_numbers = sorted(index for _, index in top_scores)
    
    return total_score, problem_numbers

# 입력 받기
scores = [int(input()) for _ in range(8)]

total_score, problem_numbers = calculate_score(scores)

print(total_score)
print(" ".join(map(str, problem_numbers)))
