import sys
input = sys.stdin.readline

input()
scores = tuple(map(int, input().rstrip().split()))

print(max(scores) - min(scores))