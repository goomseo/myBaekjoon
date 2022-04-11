import sys
input = sys.stdin.readline

# 연속된 O의 개수에 따른 점수 산출 함수
def calScore(qtyO):
    return (qtyO * (qtyO + 1)) / 2

# 테스트 케이스 개수 입력
qtyOxList = int(input())

# 테스트 케이스 입력
oxList = [input().rstrip() for _ in range(qtyOxList)]

# 각 테스트 케이스에서 X를 제외시키기
onlyO = [oxList[i].split('X') for i in range(qtyOxList)]

# 각 테스트 케이스 점수 산출 후 출력
total = 0
for j in range(qtyOxList):
    for k in range(len(onlyO[j])):
        score = calScore(onlyO[j][k].count('O'))
        total += score
    oxList[j] = total
    print(int(oxList[j]))
    total = 0
