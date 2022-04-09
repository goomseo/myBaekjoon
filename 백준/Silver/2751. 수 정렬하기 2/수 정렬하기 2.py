import sys
input = sys.stdin.readline

qtyNum = int(input())
numList = [int(input()) for _ in range(qtyNum)]
numList.sort()

for i in range(qtyNum):
    print(numList[i])