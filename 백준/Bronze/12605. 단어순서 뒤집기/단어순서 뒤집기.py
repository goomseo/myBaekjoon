import sys
input = sys.stdin.readline

N = int(input())

idx = 0
for _ in range(N):
    idx += 1
    words = input().rstrip().split()
    words.reverse()
    print(f'Case #{idx}:', ' '.join(words))