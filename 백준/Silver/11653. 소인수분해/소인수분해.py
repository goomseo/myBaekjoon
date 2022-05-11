num = int(input())

if num == 1:
    print('')
else:
    for j in range(2, (num + 1)):
        while num % j == 0:
            print(j)
            num //= j