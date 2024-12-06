import sys

input = sys.stdin.readline

num_computers = int(input())  
num_connections = int(input())  

visited_computers = [False] * (num_computers + 1)  
visited_computers[1] = True  

network = [[0] * (num_computers + 1) for _ in range(num_computers + 1)]
for _ in range(num_connections):
    a, b = map(int, input().split())
    network[a][b] = 1  
    network[b][a] = 1  
    
def dfs(network, visited_computers, current_computer):
    for i in range(len(network[0])):
        if network[current_computer][i] == 1 and not visited_computers[i]:
            visited_computers[i] = True  
            dfs(network, visited_computers, i)  

dfs(network, visited_computers, 1)  

infected_computers_count = visited_computers.count(True) - 1  

print(infected_computers_count)
