import sys
input = sys.stdin.readline

word = input().rstrip()

count_joi = 0
count_ioi = 0
for idx in range(len(word)-1):
    if word[idx:(idx + 3)] == 'JOI':
        count_joi += 1
    elif word[idx:(idx + 3)] == 'IOI':
        count_ioi += 1

print(f'{count_joi}\n{count_ioi}')