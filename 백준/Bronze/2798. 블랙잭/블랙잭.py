from itertools import combinations

def blackjack_best_sum(N, M, cards):
    
    closest_sum = 0  
    for combo in combinations(cards, 3):  
        current_sum = sum(combo)
        if closest_sum < current_sum <= M: 
            closest_sum = current_sum
        if closest_sum == M: 
            break
    return closest_sum

if __name__ == "__main__":
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))

    print(blackjack_best_sum(N, M, cards))
