import sys
input = sys.stdin.readline

for _ in range(int(input())):
    tc = input().rstrip().split()

    for word in tc:
        print(word[::-1], end = ' ')