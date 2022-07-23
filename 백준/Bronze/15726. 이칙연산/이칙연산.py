import sys
input = sys.stdin.readline

A, B, C = map(int, input().rstrip().split())
answer = max(A * B / C, A / B * C)

try:
    print(int(answer))
except:
    print(answer)