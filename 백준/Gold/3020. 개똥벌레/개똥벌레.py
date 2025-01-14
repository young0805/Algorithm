import sys
input = sys.stdin.read

def solve():
    data = input().split()
    n, h = int(data[0]), int(data[1])
    
    down = [0] * (h + 1)
    up = [0] * (h + 1)
    
    for i in range(n):
        size = int(data[2 + i])
        if i % 2 == 0: 
            down[size] += 1
        else:  
            up[size] += 1
    
    # 누적 합 계산
    for i in range(h - 1, 0, -1):
        down[i] += down[i + 1]
        up[i] += up[i + 1]
    
    min_obstacles = float('inf')
    count = 0
    
    # 각 높이에서의 파괴해야 하는 장애물 계산
    for i in range(1, h + 1):
        total = down[i] + up[h - i + 1]
        if total < min_obstacles:
            min_obstacles = total
            count = 1
        elif total == min_obstacles:
            count += 1
    
    print(min_obstacles, count)

solve()
