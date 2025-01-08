import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
pokemon_to_num = {}
num_to_pokemon = {}

for i in range(1, n + 1):
    pokemon_name = data[i]
    pokemon_to_num[pokemon_name] = i
    num_to_pokemon[i] = pokemon_name

queries = data[n + 1:]
result = []

for query in queries:
    if query.isdigit():
        result.append(num_to_pokemon[int(query)])
    else:
        result.append(pokemon_to_num[query])

print("\n".join(map(str, result)))
