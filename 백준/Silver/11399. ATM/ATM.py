import sys
input = sys.stdin.readline

input()
requiredTimes = sorted(list(map(int, input().rstrip().split())))

total = 0
for idx in range(len(requiredTimes)):
    total += sum(requiredTimes[:(idx+1)])

print(total)