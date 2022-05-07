import sys
input = sys.stdin.readline

fixedCost, variableCost, price = map(int, input().rstrip().split())

if variableCost >= price:
    print(-1)
else:
    print(int(fixedCost / (price - variableCost)) + 1)