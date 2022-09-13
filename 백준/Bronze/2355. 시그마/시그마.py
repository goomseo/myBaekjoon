import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
print(int((A + B) / 2 * (abs(B - A) + 1)))