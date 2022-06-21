import sys
input = sys.stdin.readline

input()
[print(num, end = ' ') for num in sorted(list(set(map(int, input().rstrip().split()))))]