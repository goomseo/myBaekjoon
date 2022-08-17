import sys
input = sys.stdin.readline

p1, p2 = 100, 100
for _ in range(int(input())):
    num1, num2 = map(int, input().rstrip().split())
    if num1 > num2:
        p2 -= num1
    elif num2 > num1:
        p1 -= num2

print(f'{p1}\n{p2}')