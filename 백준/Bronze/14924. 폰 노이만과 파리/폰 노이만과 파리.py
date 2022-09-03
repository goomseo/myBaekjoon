import sys
input = sys.stdin.readline

S, T, D = map(int, input().rstrip().split())
print(int(D / S / 2 * T))