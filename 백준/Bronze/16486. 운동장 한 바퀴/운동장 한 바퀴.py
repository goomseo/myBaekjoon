import sys

def input():
    return sys.stdin.readline().rstrip()

pi = 3.141592
d1, d2 = (int(input()) for _ in range(2))

print((2 * d2 * pi) + (d1 * 2))