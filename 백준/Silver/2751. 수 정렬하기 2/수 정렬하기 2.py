import sys

qtyNum = int(input())
numList = [int(sys.stdin.readline()) for i in range(qtyNum)]
numList.sort()

for j in range(qtyNum):
    print(numList[j])