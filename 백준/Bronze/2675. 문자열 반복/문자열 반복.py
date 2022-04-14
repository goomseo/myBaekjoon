import sys
input = sys.stdin.readline

qtyCase = int(input())

caseList = [input().split() for _ in range(qtyCase)]

for i in range(qtyCase):
    for j in range(len(caseList[i][1])):
        print(int(caseList[i][0]) * caseList[i][1][j], end = '')
    print()