import sys
input = sys.stdin.readline

[print(input().rstrip()[::-1]) for _ in range(list(map(int, input().rstrip().split()))[0])]