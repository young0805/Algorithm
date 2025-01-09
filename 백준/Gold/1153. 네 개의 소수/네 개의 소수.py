def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [x for x in range(limit + 1) if primes[x]]

def find_four_primes(n):
    primes = sieve_of_eratosthenes(n)
    prime_set = set(primes)
    
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                p4 = n - (p1 + p2 + p3)
                if p4 in prime_set:
                    return p1, p2, p3, p4
    return -1

n = int(input())
result = find_four_primes(n)

if result == -1:
    print(result)
else:
    print(*result)
