from math import lcm
import sys
input = sys.stdin.readline

[print(lcm(*(map(int, input().rstrip().split())))) for _ in range(int(input()))]