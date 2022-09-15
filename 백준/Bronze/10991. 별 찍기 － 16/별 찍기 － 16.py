import sys
input = sys.stdin.readline

N = int(input())

for stars in range(1, (N+1)):
    print(' ' * (N - stars), end = '')
    print(' '.join('*' * stars))