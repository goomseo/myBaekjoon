import sys
input = sys.stdin.readline

rpt = int(input())
for _ in range(rpt):
    print(sorted(list(map(int, input().rstrip().split())))[-3])