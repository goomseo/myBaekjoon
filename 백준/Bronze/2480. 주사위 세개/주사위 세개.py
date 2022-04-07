one, two, three = input().split()
diceNum = [one, two, three]
x = set(diceNum)
y = list(x)

if len(y) == 1:
    print(10000 + (int(one) * 1000))
elif len(y) == 2:
    cnt0 = diceNum.count(y[0])
    cnt1 = diceNum.count(y[1])
    if cnt0 > cnt1:
        print(1000 + (int(y[0]) * 100))
    else:
        print(1000 + (int(y[1]) * 100))
else:
    print(max(int(one), int(two), int(three)) * 100)