import sys
input = sys.stdin.readline

N = 2 * int(input()) - 1
for i in range(1, (N + 1), 2):
    print(' ' * ((N - i) // 2), end = '')
    print('*' * i)