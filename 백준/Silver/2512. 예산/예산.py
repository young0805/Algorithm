N = int(input())
budget_requests = list(map(int, input().split()))
total_budget = int(input())

if sum(budget_requests) <= total_budget:
    print(max(budget_requests))
    exit()

max_limit = 0
start, end = 0, total_budget
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for request in budget_requests:
        tmp += request if request < mid else mid

    if tmp <= total_budget:
        max_limit = max(max_limit, mid)
        start = mid + 1
    else:
        end = mid - 1

print(max_limit)
