import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
C = int(input())

print((A + B) - (C * 2) if A + B >= (C * 2) else A + B)