import sys
input = sys.stdin.readline

bottles = list(map(int, input().split()))
print(sum(bottles) * 5)