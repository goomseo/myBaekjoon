import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    counts = 0

    for a in range(1, n):
        for b in range((a + 1), n):
            result = (a ** 2 + b ** 2 + m) / (a * b)
            if  result == int(result):
                counts += 1

    print(counts)