import sys
input = sys.stdin.readline

repeatCount = int(input().rstrip())
cases = [list(map(int, input().split(','))) for _ in range(repeatCount)]

for case in cases:
    print(sum(case))