from math import ceil
import sys
input = sys.stdin.readline

day, night, height = map(int, input().rstrip().split())

print(ceil((height - night) / (day - night)))