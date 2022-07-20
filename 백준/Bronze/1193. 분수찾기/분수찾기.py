import sys
input = sys.stdin.readline

X = int(input())

n = 1
while True:
    if X <= (n * (n + 1)) / 2:
        break

    n += 1
n += 1

if n % 2 == 1:
    a = X - (((n - 2) * (n - 1)) / 2)
    print(f'{int(a)}/{int(n - a)}')
else:
    a = X - (((n - 2) * (n - 1)) / 2)
    print(f'{int(n - a)}/{int(a)}')