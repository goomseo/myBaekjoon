import sys
input = sys.stdin.readline

rBox, sBox = [int(input()) for _ in range(2)]
print(((rBox * 8) + (sBox * 3)) - 28)