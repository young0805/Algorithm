import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

heap = []
output = []

for command in data[1:]:  
    num = int(command)
    
    if num == 0:
        if heap:
            output.append(str(heapq.heappop(heap)))
        else:
            output.append('0')
    else:
        heapq.heappush(heap, num)

sys.stdout.write("\n".join(output) + "\n")
