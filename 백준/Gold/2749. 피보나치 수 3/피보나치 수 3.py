def fibonacci(N):
    a, b = 0, 1

    for _ in range(N):
        a, b = b % 1000000, (a + b) % 1000000

    return a

print(fibonacci(int(input()) % (15 * (10 ** 5))))