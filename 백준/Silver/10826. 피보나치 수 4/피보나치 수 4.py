def fibonacci(N):
    if N == 0:
        return 0
    
    a, b = 0, 1

    for _ in range(N):
        a, b = b, a + b
    
    return a

print(fibonacci(int(input())))