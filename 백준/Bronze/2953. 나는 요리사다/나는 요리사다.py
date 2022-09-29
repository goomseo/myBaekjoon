import sys
input = sys.stdin.readline

scores = [sum(map(int, input().rstrip().split())) for _ in range(5)]

print(scores.index(max(scores)) + 1, max(scores))