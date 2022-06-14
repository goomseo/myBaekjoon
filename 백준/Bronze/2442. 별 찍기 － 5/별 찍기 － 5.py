import sys

def input():
    return sys.stdin.readline().rstrip()

N = 2 * int(input()) - 1
for i in range(1, (N + 1), 2):
    print(' ' * ((N - i) // 2), end = '')
    print('*' * i)