import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

max_heap = []
result = []

for command in data[1:]:
    num = int(command)
    
    if num == 0:
        if max_heap:
            result.append(str(-heapq.heappop(max_heap)))
        else:
            result.append('0')
    else:
        heapq.heappush(max_heap, -num)

sys.stdout.write("\n".join(result) + "\n")
