from math import lcm
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
print(lcm(a, b))