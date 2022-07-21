import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
A, B = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(2)]

answer = [[A[idx], B[idx]] for idx in range(N)]

for components in answer:
    for idx in range(M):
        print(components[0][idx] + components[1][idx], end = ' ')
    
    print()