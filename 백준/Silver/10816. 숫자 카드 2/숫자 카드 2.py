import sys
input = sys.stdin.readline

input()
targets = map(int, input().rstrip().split())

count_targets = {}
for target in targets:
    if not(target in count_targets):
        count_targets[target] = 1
    else:
        count_targets[target] += 1

input()
queries = map(int, input().rstrip().split())

print(' '.join(str(count_targets[query]) if query in count_targets else '0' for query in queries))