import sys

input = sys.stdin.readline

n, m = map(int , input().split())

words = dict()
lengwords = [[] for _ in range(11)]
for i in range(n):
    word = input().strip()
    length = len(word)
    if length < m:
        continue
    if word in words:
        words[word]['count'] += 1
    else:
        words[word] = {'count':1, 'length':length}

sorted_data = [item[0] for item in sorted(
    words.items(),
    key=lambda item: (-item[1]['count'], -item[1]['length'], item[0])
)]

    
print('\n'.join(sorted_data))