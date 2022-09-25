import sys
input = sys.stdin.readline

N = int(input())

for i in range((N - 1), 0, -1):
    print(' ' * i + '*' * (2 * (N - i) - 1))

print('*' * (2 * N - 1))

for j in range(1, N):
    print(' ' * j + '*' * (2 * (N - j) - 1)) 