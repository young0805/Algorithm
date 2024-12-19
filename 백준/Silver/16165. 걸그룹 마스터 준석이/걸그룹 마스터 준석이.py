N, M = map(int, input().split())

team_info = {}
member_info = {}

for _ in range(N):
    team_name = input().strip()  
    num_members = int(input().strip())  
    members = []
    
    for _ in range(num_members):
        member_name = input().strip()
        members.append(member_name)
        member_info[member_name] = team_name 
    
    team_info[team_name] = sorted(members)  

# 퀴즈 처리
for _ in range(M):
    query = input().strip()  # 퀴즈 질문 (팀 이름 또는 멤버 이름)
    quiz_type = int(input().strip())  # 퀴즈 종류 (0: 팀 -> 멤버, 1: 멤버 -> 팀)
    
    if quiz_type == 0:
        # 팀 이름 -> 해당 팀 멤버 출력
        members = team_info[query]
        for member in members:
            print(member)
    elif quiz_type == 1:
        # 멤버 이름 -> 해당 멤버가 속한 팀 출력
        team_name = member_info[query]
        print(team_name)
