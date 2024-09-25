# 백준 2606번 문제 풀이

c = int(input()) # 컴퓨터 수
n = int(input()) # 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(c + 1)] # 연결 정보 담을 그래프 초기화

for _ in range(n):
    com1, com2 = map(int, input().split()) # 연결된 컴퓨터 번호 쌍
    # 방향이 정해져 있지 않으므로 컴퓨터마다 양방향으로 정보 저장
    graph[com1].append(com2)
    graph[com2].append(com1)

visited = [False]* (c + 1) # 방문 여부 표시할 리스트

def dfs(n): # 그래프 깊이 탐색 함수
    visited[n] = True # 바이러스가 n번 컴퓨터에 방문했음을 표시
    for v in graph[n]: # graph[n]은 n번 컴퓨터와 연결된 컴퓨터 리스트
        if visited[v] is False: # 방문하지 않았을 경우 함수 재귀 호출
            dfs(v)

dfs(1) # 1번 컴퓨터부터 시작
print(visited.count(True) - 1) # 1번 컴퓨터 제외하고 연결된 컴퓨터 수 출력
