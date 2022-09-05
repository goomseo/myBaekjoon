import sys
input = sys.stdin.readline

for _ in range(int(input())):
    R, E, C = map(int, input().rstrip().split())
    
    if R < E - C:
        print("advertise")
    elif R == E - C:
        print("does not matter")
    else:
        print("do not advertise")