n = int(input())  # 카드의 개수 N을 입력받음

from collections import deque
cards = deque()  # 카드를 저장할 덱 (deque)

# 카드 번호 1부터 N까지 덱에 추가
for i in range(1, n + 1):
    cards.append(i)

# 덱에 카드가 하나 남을 때까지 반복
while len(cards) > 1:
    cards.popleft()  # 제일 위에 있는 카드를 버림
    cards.append(cards.popleft())  # 제일 위에 있는 카드를 제일 아래로 옮김

# 남은 카드 출력
print(cards[0])
