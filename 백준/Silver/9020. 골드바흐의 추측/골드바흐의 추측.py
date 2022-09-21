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

for _ in range(int(input())):
    N = int(input())
    
    lst = []
    for num in range(2, (N // 2 + 1)):
        if isPrimeNum(num):
            lst.append(num)
    lst.reverse()

    for num in lst:
        if isPrimeNum(N - num):
            print(num, N - num)
            break