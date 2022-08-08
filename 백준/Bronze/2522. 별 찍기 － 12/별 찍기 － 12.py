import sys
input = sys.stdin.readline

N = int(input())

for stars in range(1, (N + 1)):
    print(' ' * (N - stars) + '*' * stars)

for stars in range((N - 1), 0, -1):
    print(' ' * (N - stars) + '*' * stars)