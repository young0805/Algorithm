import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

def get_sums(arr):
    result = [0]
    for num in arr:
        temp = []
        for s in result:
            if s + num <= c:
                temp.append(s + num)
        result.extend(temp)
    return result

a, b = arr[:n//2], arr[n//2:]
s1, s2 = get_sums(a), get_sums(b)
s2.sort()

count = 0
for x in s1:
    left, right = 0, len(s2)
    while left < right:
        mid = (left + right) // 2
        if s2[mid] + x <= c:
            left = mid + 1
        else:
            right = mid
    count += left

print(count)
