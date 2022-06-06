from math import sqrt
import sys
input = sys.stdin.readline

n = int(input())
print(int((5 ** -0.5) * ((((1 + sqrt(5)) * 0.5) ** n) - (((1 - sqrt(5)) * 0.5) ** n))))