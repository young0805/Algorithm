import sys
input = sys.stdin.readline

n = int(input())
count = 0  
current = 666  

while count < n:
    if "666" in str(current):
        count += 1
    current += 1

print(current - 1)
