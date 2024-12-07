from collections import deque

subin_position, sibling_position = map(int, input().split())

queue = deque()
queue.append(subin_position)

# time_to_reach[i]는 위치 i에 도달하는 데 걸린 시간
time_to_reach = [-1] * 100001
time_to_reach[subin_position] = 0

while queue:
    current_position = queue.popleft()

    # 동생을 찾았다면 걸린 시간 출력 후 종료
    if current_position == sibling_position:
        print(time_to_reach[current_position])
        break

    # 이동할 수 있는 세 가지 위치
    for next_position in [current_position - 1, current_position + 1, current_position * 2]:
        if 0 <= next_position <= 100000 and time_to_reach[next_position] == -1:
            time_to_reach[next_position] = time_to_reach[current_position] + 1
            queue.append(next_position)
