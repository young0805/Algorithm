from itertools import combinations

def count_subsequences(n, target, nums):
    count = 0
    for size in range(1, n + 1):
        for subset in combinations(nums, size):
            if sum(subset) == target:
                count += 1
    return count

def process_input(input_data):
    lines = input_data.strip().splitlines()
    n, target = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))
    return n, target, nums

def main():
    import sys
    input_data = sys.stdin.read()
    n, target, nums = process_input(input_data)
    print(count_subsequences(n, target, nums))

if __name__ == "__main__":
    main()
