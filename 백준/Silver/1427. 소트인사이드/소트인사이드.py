# 내림차순 정렬: (reverse = True)
# end=''를 이용하면 한 줄씩 출력되어야 할 i를 띄어쓰기 없이 출력

number = input()

array = sorted(list(number), reverse=True)

for i in range(len(array)):
  print(array[i], end='')