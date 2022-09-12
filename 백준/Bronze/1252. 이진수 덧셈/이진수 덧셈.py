import sys
input = sys.stdin.readline

x, y = input().rstrip().split()

print(bin(int(x, 2) + int(y, 2))[2:])