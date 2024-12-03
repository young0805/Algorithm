N =int(input())
members = []

for i in range(N):
    age, name = input().split()
    members.append([int(age),name])

# sort 함수에 key 여러개 기입 + lambda 활용
# python에서는 정렬 기준을 함수로 지정할 수 있기 때문에, lambda 함수를 이용해 간단하게 나이를 기준으로 정렬

for j in sorted(members, key=lambda x : x[0]):
    print(j[0],j[1])