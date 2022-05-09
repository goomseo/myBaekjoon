import sys
input = sys.stdin.readline

def isPrimeNum(naturalNum):
    if naturalNum == 1:
        return False

    for num in range(2, naturalNum):
        if naturalNum % num == 0:
            return False
    
    return True

def main():
    low, high = [int(input()) for _ in range(2)]

    primeNums = []
    for n in range(low, (high + 1)):
        if isPrimeNum(n) == True:
            primeNums.append(n)
    
    if primeNums:
        print(sum(primeNums))
        print(min(primeNums))
    else:
        print(-1)

main()