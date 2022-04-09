import sys

numList = [int(sys.stdin.readline()) for i in range(10)]
modResult = [numList[j] % 42 for j in range(10)]
cntDiffMod = len(list(set(modResult)))

print(cntDiffMod)