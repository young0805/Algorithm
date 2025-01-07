from collections import deque

queue = deque([i for i in range(1,int(input())+1)])

while queue:
    print(queue.popleft(),end=" ")
    if queue:
        queue.append(queue.popleft())