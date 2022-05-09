from math import sqrt
import sys
input = sys.stdin.readline

def isPrimeNum(naturalNum):
    if naturalNum == 1:
        return False
    else:
        for num in range(2, (int(sqrt(naturalNum)) + 1)):
            if naturalNum % num == 0:
                return False

        return True

def main():
    LOW, HIGH = map(int, input().rstrip().split())
    
    for num in range(LOW, (HIGH + 1)):
        if isPrimeNum(num):
             print(num)

main()