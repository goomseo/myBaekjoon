a, b = map(int, input().split())

if a < b:
    print(-1)
else:
    c, d = (a + b) // 2, (a - b) // 2

    if (c + d == a) and (c - d == b):
        print(c, d)
    else:
        print(-1)