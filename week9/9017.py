t = int(input())
for _ in range(t):
    n = int(input())
    count = {} 
    temp = list(map(int, input().split()))

    # 각 팀별 선수 수 세기
    for i in range(n):
        if temp[i] in count:
            count[temp[i]] += 1
        else:
            count[temp[i]] = 1

    # 6명 미만인 팀 제거
    dele = {}
    for k, v in count.items():
        if v < 6:
            dele[k] = 1

    team = {}
    idx = 1  # 등수 카운팅

    # 팀 구성
    for i in range(n):
        if temp[i] not in dele:  # 6명 이상인 팀만 처리
            if temp[i] in team:
                if team[temp[i]][0] < 4:  # 4명까지의 합산
                    team[temp[i]][0] += 1
                    team[temp[i]][1] += idx
                elif team[temp[i]][0] == 4:  # 5번째 팀원 처리
                    team[temp[i]][0] += 1
                    team[temp[i]][2] = idx
            else:
                team[temp[i]] = [1, idx, 0]  # 첫 팀원 처리

            idx += 1

    # 팀 6명인지 체크
    valid_teams = {k: v for k, v in team.items() if v[0] == 5}

    # 정렬 및 출력
    if valid_teams:
        sorted_team = sorted(valid_teams.items(), key=lambda x: (x[1][1], x[1][2]))
        print(sorted_team[0][0])  # 첫 번째 팀 출력
    else:
        print("No valid teams")
