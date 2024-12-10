n = int(input())  # 도시의 개수
distances = list(map(int, input().split()))  # 각 도시 간 도로의 길이
fuel_prices = list(map(int, input().split()))  # 각 도시의 주유소 리터당 가격

total_cost = 0  # 총 비용
current_price = fuel_prices[0]  # 첫 번째 도시에서의 리터당 가격

for i in range(n-1):
    if fuel_prices[i] < current_price:  # 더 싼 기름 가격이 나오면 갱신
        current_price = fuel_prices[i]
    
    total_cost += current_price * distances[i]  # 이동 거리 * 현재 가격만큼 비용 추가

print(total_cost)  # 최소 비용 출력
