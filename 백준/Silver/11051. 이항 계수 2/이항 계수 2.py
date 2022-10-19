from math import comb
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
print(comb(N, K) % 10007)