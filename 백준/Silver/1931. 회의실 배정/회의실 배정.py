import sys

n = int(input())  # 회의의 수

meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 종료 시간을 오름차순으로 정렬하고, 종료 시간이 같으면 시작 시간을 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

current_time = 0  # 회의가 끝난 시간
max_meetings = 0  # 최대 회의 수

for start, end in meetings:
    if current_time <= start:  # 회의가 가능한 시간인지 확인
        current_time = end  # 회의가 끝난 시간으로 갱신
        max_meetings += 1  # 회의 수 증가

print(max_meetings)
