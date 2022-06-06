import sys
input = sys.stdin.readline

studentNums = sorted([int(input().rstrip()) for _ in range(28)])

for num in range(1, 31):
    if num not in studentNums:
        print(num)