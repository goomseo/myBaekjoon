import sys
input = sys.stdin.readline

n = int(input())

birds = 1
seconds = 0
while True:
    if not n:
        break

    if n >= birds:
        n -= birds
        birds += 1
        seconds += 1
    else:
        birds = 1
        n -= birds
        birds += 1
        seconds += 1

print(seconds)