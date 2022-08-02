n, F = (int(input()) for _ in range(2))

n -= n % 100
while True:
    if n % F:
        n += 1
    else:
        break

print(str(n)[-2:])