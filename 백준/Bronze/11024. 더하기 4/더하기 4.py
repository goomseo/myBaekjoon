import sys
input = sys.stdin.readline

[print(sum(map(int, input().rstrip().split()))) for _ in range(int(input()))]