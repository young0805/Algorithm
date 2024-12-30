def k_swaps(n, k, li):
    sorted_li = sorted(li)
    index_map = {value: idx for idx, value in enumerate(li)}
    
    for i in range(n - 1, -1, -1):
        if li[i] != sorted_li[i]:
            to_swap = sorted_li[i]
            li[i], li[index_map[to_swap]] = li[index_map[to_swap]], li[i]
            index_map[li[index_map[to_swap]]], index_map[to_swap] = index_map[to_swap], i
            k -= 1
            if k == 0:
                return li
    return -1

n, k = map(int, input().split())
li = list(map(int, input().split()))
result = k_swaps(n, k, li)
print(" ".join(map(str, result)) if result != -1 else -1)
