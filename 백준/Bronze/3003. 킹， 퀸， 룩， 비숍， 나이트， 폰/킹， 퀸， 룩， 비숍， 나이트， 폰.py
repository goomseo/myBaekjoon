import sys
input = sys.stdin.readline

pieces = list(map(int, input().split()))
rightQuantities = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(rightQuantities[i] - pieces[i], end = ' ')