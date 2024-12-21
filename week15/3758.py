import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    logs = [list(map(int, input().split())) for _ in range(m)]

    scores = dict()  # 점수
    counts = dict()   # 제출 횟수
    stime = dict()   # 제출 시간

    for i in range(len(logs)):
        tid, pid, score = logs[i]

        if tid not in scores:
            scores[tid] = [0] * (k + 1)
        scores[tid][pid] = max(scores[tid][pid], score)

        if tid not in counts:
            counts[tid] = 0
        counts[tid] += 1

        stime[tid] = i

    answer = []
    for tid in scores.keys():
        total = sum(scores[tid])
        answer.append([total, counts[tid], stime[tid], tid])

    answer.sort(key=lambda x: (-x[0], x[1], x[2]))

    rank = 1
    for data in answer:
        if data[3] == t:
            print(rank)
            break
        rank += 1
