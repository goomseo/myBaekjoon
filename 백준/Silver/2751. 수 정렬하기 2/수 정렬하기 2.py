import sys
input = sys.stdin.readline
print = sys.stdout.write

qtyNum = int(input())
numList = [int(input()) for _ in range(qtyNum)]
numList.sort()

for i in range(qtyNum):
    print(str(numList[i]) + '\n')