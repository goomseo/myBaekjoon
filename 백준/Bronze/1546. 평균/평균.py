import statistics
import sys
input = sys.stdin.readline

qtySubject = int(input())
scoreList = list(map(int, input().split()))

scoreList = [scoreList[i] / max(scoreList) * 100 for i in range(qtySubject)]
print(statistics.mean(scoreList))
