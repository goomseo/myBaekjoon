import math
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().rstrip().split())
    print(math.lcm(A, B), math.gcd(A, B))