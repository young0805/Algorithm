N = int(input())  # 타일의 길이 N
tile_ways = [0, 1, 2]  # 타일을 채우는 방법 수 초기화 (길이가 1일 때 1가지, 길이가 2일 때 2가지 방법)

for i in range(3, N+1):
    tile_ways.append(tile_ways[i-1] + tile_ways[i-2])  # 이전 두 경우의 합으로 현재 방법 수 계산

print(tile_ways[N] % 10007)  # N 길이에 대한 방법 수를 10007로 나눈 나머지 출력
