import sys
input = sys.stdin.readline

S = int(input())

n = 0
while True:
    if (n * (n + 1)) / 2 > S:
        break
    n += 1

print(n - 1)