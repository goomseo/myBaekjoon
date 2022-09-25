import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N):
    print('*' * i + ' ' * (2 * (N - i)) + '*' * i)

print('*' * (2 * N))

for j in range((N - 1), 0, -1):
    print('*' * j + ' ' * (2 * (N - j)) + '*' * j)