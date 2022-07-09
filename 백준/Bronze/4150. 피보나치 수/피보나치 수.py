def fibo(N):
    a, b = 0, 1 
    for _ in range(int(N)):
        a, b = b, a + b

    return a

print(fibo(input()))