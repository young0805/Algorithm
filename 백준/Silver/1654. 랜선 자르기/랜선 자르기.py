import sys

K, N = map(int, sys.stdin.readline().strip().split())

lan_lengths = []
for _ in range(K):
    lan_lengths.append(int(sys.stdin.readline().strip()))

start, end = 1, max(lan_lengths)

while start <= end:
    mid = (start + end) // 2  
    total_lan_count = 0  
    
    for length in lan_lengths:
        total_lan_count += length // mid

    if total_lan_count >= N:
        start = mid + 1
    else:          
        end = mid - 1

print(end)
