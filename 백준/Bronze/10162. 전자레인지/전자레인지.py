import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    secs = int(input())

    if secs % 10 != 0:
        print(-1)
        break

    for i in (300, 60, 10):
        print(secs // i, end = ' ')
        secs %= i

    break