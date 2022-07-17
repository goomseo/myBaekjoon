import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    print('yes' if 6 <= len(input().rstrip()) <= 9 else 'no')