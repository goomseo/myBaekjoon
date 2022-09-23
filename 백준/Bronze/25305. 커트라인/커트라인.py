import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
scores = sorted(list(map(int, input().rstrip().split())), reverse = True)

print(scores[K-1])