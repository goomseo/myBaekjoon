import sys
input = sys.stdin.readline

x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())

if (y3 - y2) * (x2 - x1) > (y2 - y1) * (x3 - x2):
    print(1)
elif (y3 - y2) * (x2 - x1) < (y2 - y1) * (x3 - x2):
    print(-1)
else:
    print(0)