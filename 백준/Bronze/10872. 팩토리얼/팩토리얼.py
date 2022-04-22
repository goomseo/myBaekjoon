def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

limitNum = int(input())
print(factorial(limitNum))