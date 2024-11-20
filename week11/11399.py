N = int(input())

peoples = list(map(int, input().split()))
peoples.sort()

answer = [peoples[0]]
for i in range(1,N):
    answer.append(answer[i-1] + peoples[i])

print(sum(answer))