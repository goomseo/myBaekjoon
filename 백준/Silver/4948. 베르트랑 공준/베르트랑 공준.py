import sys
input = sys.stdin.readline

def isPrimeNum(naturalNum):
    if naturalNum == 1:
        return False
    else:
        for num in range(2, (int(naturalNum ** 0.5) + 1)):
            if naturalNum % num == 0:
                return False

        return True

primeNums = 0
while True:
    N = int(input())

    if not N:
        break

    for num in range((N + 1), (2 * N + 1)):
        if isPrimeNum(num):
            primeNums += 1

    print(primeNums)
    primeNums = 0