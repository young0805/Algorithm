# 브루트포스 알고리즘: 완전 탐색 알고리즘. 가능한 모든 경우의 수를 모두 탐색하면서 요구 조건에 충족되는 결과 찾음
# 종류: 선형 구조 - 순차 탐색/ 비선형 구조 - DFS, BFS
# 대표 문제: 10 약수의 합 구하기, 거스름돈을 지불할 수 있는 방법의 수와 최소 동전의 개수 구하기
# 브루트포스의 장점: 알고리즘을 설계하고 구현하기 쉽다, 모든 경우의 수를 탐색하기 때문에 100% 정확성을 보장한다.
# 브루트포스의 단점: 메모리 효율면에서 매우 비효율적이다, 알고리즘의 실행 시간이 매우 오래걸린다. (시간복잡도가 높다)

array = []
for i in range(9):
    array.append(int(input()))

array.sort()

Total = sum(array)

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if Total - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            exit()