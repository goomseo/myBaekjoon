import sys
input = sys.stdin.readline

start, end = [int(input()) for _ in range(2)]

squareNums = []
for num in range(start, (end + 1)):
    if (num ** 0.5) % 1 == 0:
        squareNums.append(num)

print(f'{sum(squareNums)}\n{min(squareNums)}' if len(squareNums) else -1)