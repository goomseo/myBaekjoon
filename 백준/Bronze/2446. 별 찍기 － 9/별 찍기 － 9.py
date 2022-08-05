import sys
input = sys.stdin.readline

N = 2 * int(input()) - 1

for stars in range(N, 0, -2):
    spaces = (N - stars) // 2
    print(' ' * spaces + '*' * stars)

for stars in range(3, (N + 1), 2):
    spaces = (N - stars) // 2
    print(' ' * spaces + '*' * stars)