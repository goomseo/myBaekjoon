import sys
input = sys.stdin.readline

numList = [int(input()) for _ in range(10)]
modResult = [numList[j] % 42 for j in range(10)]
cntDiffMod = len(set(modResult))

print(cntDiffMod)