import sys

input = sys.stdin.readline

num_groups, num_quizzes = map(int, input().split())

group_members = {}
member_to_group = {}

for _ in range(num_groups):
    group_name = input().strip() 
    num_members = int(input().strip())  
    members_list = []  
    
    for _ in range(num_members):
        member_name = input().strip()
        members_list.append(member_name) 
        member_to_group[member_name] = group_name  

    members_list.sort()  
    group_members[group_name] = members_list  

def handle_quiz(query, quiz_type):
    if quiz_type == 1:
        group_name = member_to_group[query]
        print(group_name)
    elif quiz_type == 0:
        members = group_members[query]
        for member in members:
            print(member)

for _ in range(num_quizzes):
    quiz_query = input().strip() 
    quiz_type = int(input().strip()) 
    handle_quiz(quiz_query, quiz_type)  
