schools = int(input())
leftover = 0

for _ in range(schools):
    students, apples = map(int, input().split())
    leftover += apples % students

print(leftover)
