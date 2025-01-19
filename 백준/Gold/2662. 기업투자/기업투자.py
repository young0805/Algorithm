total_money, num_companies = map(int, input().split())
profit_table = [list(map(int, input().split()))[1:] for _ in range(total_money)]

max_profit = [[0] * (total_money + 1) for _ in range(num_companies + 1)]
investment = [[0] * (total_money + 1) for _ in range(num_companies + 1)]

for comp in range(1, num_companies + 1):
    for money in range(1, total_money + 1):
        max_profit[comp][money] = max_profit[comp - 1][money]
        for invest in range(1, money + 1):
            if max_profit[comp][money] < max_profit[comp - 1][money - invest] + profit_table[invest - 1][comp - 1]:
                max_profit[comp][money] = max_profit[comp - 1][money - invest] + profit_table[invest - 1][comp - 1]
                investment[comp][money] = invest

print(max_profit[num_companies][total_money])

allocations = [0] * num_companies
remaining_money = total_money
for comp in range(num_companies, 0, -1):
    allocations[comp - 1] = investment[comp][remaining_money]
    remaining_money -= investment[comp][remaining_money]

print(" ".join(map(str, allocations)))
