import sys
input = sys.stdin.readline

def findPrimeNum(naturalNum):
    if naturalNum == 1:
        return False

    for num in range(2, naturalNum):
        if naturalNum % num == 0:
            return False
    
    return True

def main():
    input()
    nums = map(int, input().rstrip().split())

    qtyPrimeNum = 0
    for num in nums:
        if findPrimeNum(num) == True:
            qtyPrimeNum += 1

    print(qtyPrimeNum)

main()