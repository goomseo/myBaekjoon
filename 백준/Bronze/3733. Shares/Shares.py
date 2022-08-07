import sys
input = sys.stdin.readline

while True:
    try:
        N, S = map(int, input().rstrip().split())
        print(S // (N + 1))
    except:
        break