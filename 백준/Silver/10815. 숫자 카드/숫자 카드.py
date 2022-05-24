import sys
input = sys.stdin.readline

input()
cmpObjects = set(map(int, input().rstrip().split()))
input()
objects = list(map(int, input().rstrip().split()))

for num in objects:
    if num in cmpObjects:
        print(1, end = ' ')
    else:
        print(0, end = ' ')