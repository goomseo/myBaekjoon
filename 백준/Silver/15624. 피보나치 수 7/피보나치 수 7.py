def fibonacci(N):
    a, b = 0, 1

    for _ in range(N):
        a, b = b % 1000000007, (a + b) % 1000000007

    return a

print(fibonacci(int(input())))