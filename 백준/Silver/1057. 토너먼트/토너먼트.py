def find_round(n, a, b):
    count = 0
    while a != b:
        count += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
    return count

def main():
    import sys
    input = sys.stdin.read
    n, a, b = map(int, input().split())
    print(find_round(n, a, b))

if __name__ == "__main__":
    main()
