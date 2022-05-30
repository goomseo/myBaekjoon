import sys
input = sys.stdin.readline

scores = [int(input().rstrip()) for _ in range(6)]

print((sum(scores[:4]) - min(scores[:4])) + max(scores[4:]))