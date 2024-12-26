def suffix_array(S):
    suffixes = [S[i:] for i in range(len(S))]
    suffixes.sort()

    for suffix in suffixes:
        print(suffix)

S = input()

suffix_array(S)
