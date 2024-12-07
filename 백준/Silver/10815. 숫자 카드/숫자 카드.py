num_cards_count = int(input())  # 상근이가 가진 카드의 개수
owned_cards = list(map(int, input().split()))  # 상근이가 가진 카드 리스트
query_count = int(input())  # 질문할 카드의 개수
queries = list(map(int, input().split()))  # 질문할 카드 리스트

owned_cards.sort()  # 숫자 카드 정렬

low, high = 0, num_cards_count - 1  # 이진 탐색 범위 설정

def binary_search(cards, low, high, target):  # 이진 탐색 함수
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] == target:
            return mid
        if cards[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None  # 찾지 못한 경우

for query in queries:
    if binary_search(owned_cards, low, high, query) is not None:
        print(1, end=" ")  # 카드를 가지고 있다면 1 출력
    else:
        print(0, end=" ")  # 카드를 가지고 없다면 0 출력
