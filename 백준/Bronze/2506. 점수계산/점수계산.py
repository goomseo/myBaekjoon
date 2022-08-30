import sys
input = sys.stdin.readline

input()
results = ''.join(input().rstrip().split()).split('0')

totalScore = 0
for result in results:
    totalScore += (1 + len(result)) / 2 * len(result)

print(int(totalScore))