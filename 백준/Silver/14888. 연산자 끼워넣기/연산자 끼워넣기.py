N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

INF = int(1e9)

def calculate(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        return a // b if a >= 0 else -(-a // b)

def dfs(index, result, operators):
    if index == N:
        return result, result
    
    max_val = -INF
    min_val = INF

    for i in range(4):
        if operators[i] > 0:
            next_operators = operators[:]
            next_operators[i] -= 1
            new_result = calculate(result, nums[index], i)
            max_tmp, min_tmp = dfs(index + 1, new_result, next_operators)
            
            max_val = max(max_val, max_tmp)
            min_val = min(min_val, min_tmp)
    
    return max_val, min_val

max_result, min_result = dfs(1, nums[0], operators)
print(max_result)
print(min_result)
