import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    stars = ' '.join((['*'] * N))

    print(stars if (i + 1) % 2 else ' ' + stars)