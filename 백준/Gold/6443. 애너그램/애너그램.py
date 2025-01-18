def find_anagrams(chars, used, current, results):
    if len(current) == len(chars):
        results.append("".join(current))
        return

    prev = None
    for i in range(len(chars)):
        if not used[i] and chars[i] != prev:
            used[i] = True
            current.append(chars[i])
            find_anagrams(chars, used, current, results)
            current.pop()
            used[i] = False
            prev = chars[i]

t = int(input())
for _ in range(t):
    word = input().strip()
    chars = sorted(word)
    used = [False] * len(chars)
    results = []
    find_anagrams(chars, used, [], results)
    print("\n".join(results))
