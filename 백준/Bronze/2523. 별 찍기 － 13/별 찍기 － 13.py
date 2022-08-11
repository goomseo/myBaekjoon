import sys
input = sys.stdin.readline

N = int(input())

[print('*' * stars) for stars in range(1, N)]
[print('*' * stars) for stars in range(N, 0, -1)]