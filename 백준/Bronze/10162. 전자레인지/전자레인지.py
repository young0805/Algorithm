T = int(input())

A, B, C = 300, 60, 10

if T % C != 0:
    print(-1)
else:
    a_count = T // A
    T %= A
    b_count = T // B
    T %= B
    c_count = T // C
    print(a_count, b_count, c_count)
