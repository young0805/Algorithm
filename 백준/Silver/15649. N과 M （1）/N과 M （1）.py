from itertools import permutations

def generate_permutations(n, m):
    return list(permutations(range(1, n + 1), m))

def solve_and_print(n, m):
    permutations_list = generate_permutations(n, m)
    for permutation in permutations_list:
        print(" ".join(map(str, permutation)))

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip()
    n, m = map(int, input_data.split())
    solve_and_print(n, m)
