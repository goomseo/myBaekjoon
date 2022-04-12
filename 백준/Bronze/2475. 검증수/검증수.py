import sys
input = sys.stdin.readline

numList = list(map(int, input().split()))

total = 0
for i in range(len(numList)):
    total += numList[i] ** 2

print(total % 10)