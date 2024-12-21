def calculate_ranks(n, people):
    ranks = []
    for i in range(n):
        rank = 1
        for j in range(n):
            if i != j:
                if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                    rank += 1
        ranks.append(rank)
    return ranks

if __name__ == "__main__":
    n = int(input())
    people = [tuple(map(int, input().split())) for _ in range(n)]
    ranks = calculate_ranks(n, people)
    print(" ".join(map(str, ranks)))
