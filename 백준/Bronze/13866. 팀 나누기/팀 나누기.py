import sys
input = sys.stdin.readline

A, B, C, D = map(int, input().split())

gaps = [[A + B, C + D], [A + C, B + D], [A + D, B + C]]
for idx in range(len(gaps)):
    gaps[idx] = max(gaps[idx]) - min(gaps[idx])

print(min(gaps))