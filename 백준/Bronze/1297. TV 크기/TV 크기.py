from math import sqrt
import sys
input = sys.stdin.readline

d, hRatio, wRatio = map(int, input().rstrip().split())

h = sqrt(d**2/(1 + (wRatio**2/hRatio**2)))
w = wRatio / hRatio * h
print(int(h), int(w))