from math import log2
import sys
input = sys.stdin.readline

N = log2(int(input()))
print(1 if N == int(N) else 0)