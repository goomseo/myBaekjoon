import sys
input = sys.stdin.readline

h, m, s = map(int, input().rstrip().split())

cookingTime = int(input().rstrip())

endTime = (h * 3600) + (m * 60) + s + cookingTime

for n in range(6, -1, -1):
    if (endTime - (3600 * 24 * n)) >= 0:
        endTime -= 3600 * 24 * n

print(endTime // 3600, endTime % 3600 // 60, endTime % 3600 % 60)