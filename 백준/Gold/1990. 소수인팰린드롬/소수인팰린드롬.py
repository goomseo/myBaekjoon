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

a, b = map(int, input().rstrip().split())
if b >= 10000000:
    b = 9989899

lst = [num for num in range(a, (b + 1)) if ((num % 2) and (num == int(str(num)[::-1])))]
[print(num) for num in lst if isPrimeNum(num)]

print(-1)