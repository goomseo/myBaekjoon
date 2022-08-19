import sys
input = sys.stdin.readline

def getMin(num):
    return int(num.replace('6', '5'))

def getMax(num):
    return int(num.replace('5', '6'))

a, b = input().rstrip().split()

print(getMin(a) + getMin(b), getMax(a) + getMax(b))