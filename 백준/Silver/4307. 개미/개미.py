# 막대 길이와 개미들의 위치를 받아 가장 빠른 시간과 가장 느린 시간을 계산하는 함수.
def calculate_times(l, positions):
    min_time = max(min(pos, l - pos) for pos in positions)
    max_time = max(max(pos, l - pos) for pos in positions)
    return min_time, max_time

# 문제를 해결하고 결과를 출력하는 메인 함수
def solve_ants_problem():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 테스트 케이스 처리
    t = int(data[0])
    results = []
    idx = 1
    for _ in range(t):
        l, n = int(data[idx]), int(data[idx + 1])
        idx += 2
        positions = list(map(int, data[idx:idx + n]))
        idx += n
        results.append(calculate_times(l, positions))
    
    # 결과 출력
    for min_time, max_time in results:
        print(min_time, max_time)

solve_ants_problem()
