import sys
input = sys.stdin.readline

diceNums = list(map(int, input().rstrip().split()))
cmp = list(set(diceNums))

if len(cmp) == 1:
    print(10000 + (cmp[0] * 1000))
elif len(cmp) == 2:
    for n in cmp:
        if diceNums.count(n) == 2:
            print(1000 + (n * 100))
            break
elif len(cmp) == 3:
    print(max(cmp) * 100)