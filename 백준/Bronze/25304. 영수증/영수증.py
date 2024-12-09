total_amount = int(input())  # 영수증에 적힌 총 금액
item_count = int(input())    # 구매한 물건의 종류 수
calculated_total = 0         # 계산된 총 금액

for _ in range(item_count):  
    price, quantity = map(int, input().split())  # 물건 가격과 개수 입력
    calculated_total += price * quantity         # 총 금액에 추가

if calculated_total == total_amount:             # 계산된 총 금액과 영수증 금액 비교
    print("Yes")
else:
    print("No")
