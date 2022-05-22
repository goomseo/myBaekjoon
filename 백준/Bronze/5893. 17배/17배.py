import sys
input = sys.stdin.readline

n = '0b' + input().rstrip()
print(bin(int(n, 2) * 17)[2:])