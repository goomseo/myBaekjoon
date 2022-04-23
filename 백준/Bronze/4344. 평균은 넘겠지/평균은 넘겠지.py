import sys
input = sys.stdin.readline

qtyCase = int(input())
caseList = []

for _ in range(qtyCase):
    caseList.append(list(map(int, input().split())))

qualifiedScoresList = []
for i in range(len(caseList)):
    avg = (sum(caseList[i]) - caseList[i][0]) / (len(caseList[i]) - 1)

    for j in range(1, len(caseList[i])):
        if caseList[i][j] > avg:
            qualifiedScoresList.append(caseList[i][j])

    percentage = (len(qualifiedScoresList) / (len(caseList[i]) - 1)) * 100
    print(f'{percentage:0.3f}%')

    qualifiedScoresList = []
    