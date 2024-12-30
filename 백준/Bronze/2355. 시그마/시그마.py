a, b = map(int, input().split())

if a > b:
    a, b = b, a  # 항상 a <= b가 되도록 정렬
    
result = (b - a + 1) * (a + b) // 2  # 등차수열 합 공식
print(result)
