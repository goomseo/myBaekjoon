import sys
input = sys.stdin.readline

a, b = input().rstrip().split()

getMin = lambda num: int(num.replace('6', '5'))
getMax = lambda num: int(num.replace('5', '6'))

print(getMin(a) + getMin(b), getMax(a) + getMax(b))