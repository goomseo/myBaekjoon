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

num = int(input())
while True:
    if (str(num) == str(num)[::-1]) and (isPrimeNum(num)):
        print(num)
        break

    num += 1