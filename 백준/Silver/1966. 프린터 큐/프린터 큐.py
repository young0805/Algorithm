t = int(input())

for _ in range(t):
    n, target = map(int, input().split())
    pri = list(map(int, input().split()))
    
    idx = list(range(n))  
    count = 0  

    while True:
        if pri[0] == max(pri):  
            count += 1
            if idx[0] == target:  
                print(count)
                break
            pri.pop(0)
            idx.pop(0)
        else:  
            pri.append(pri.pop(0))
            idx.append(idx.pop(0))
