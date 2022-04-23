import sys
input = sys.stdin.readline

peopleSqMeter, extent = map(int, input().split())
numOfPeople = peopleSqMeter * extent

articleNum = list(map(int, input().split()))

for i in range(5):
    print(articleNum[i] - numOfPeople, end = ' ')