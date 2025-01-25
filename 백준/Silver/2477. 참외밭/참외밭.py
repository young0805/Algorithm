k = int(input())
data = [tuple(map(int, input().split())) for _ in range(6)]

w = 0
w_idx = 0
h = 0
h_idx = 0

for i in range(6):
    d, l = data[i]
    if d == 1 or d == 2:
        if l > w:
            w = l
            w_idx = i
    elif d == 3 or d == 4:
        if l > h:
            h = l
            h_idx = i

big = w * h

small_w = abs(data[(w_idx - 1) % 6][1] - data[(w_idx + 1) % 6][1])
small_h = abs(data[(h_idx - 1) % 6][1] - data[(h_idx + 1) % 6][1])
small = small_w * small_h

print((big - small) * k)
