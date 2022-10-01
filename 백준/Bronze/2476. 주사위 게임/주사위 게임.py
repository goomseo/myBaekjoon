import sys
input = sys.stdin.readline

prize = []
for _ in range(int(input())):
    dice_map = map(int, input().rstrip().split())
    
    diceCount_1 = dict()
    for dice in dice_map:
        if not(dice in diceCount_1):
            diceCount_1[dice] = 1
        else:
            diceCount_1[dice] += 1

    diceCount_2 = {3: [], 2: [], 1: []}
    for dice in diceCount_1.keys():
        if diceCount_1[dice] == 3:
            diceCount_2[3].append(dice)
        elif diceCount_1[dice] == 2:
            diceCount_2[2].append(dice)
        else:
            diceCount_2[1].append(dice)

    if len(diceCount_2[3]):
        prize.append(1000 * (10 + diceCount_2[3][0]))
    elif len(diceCount_2[2]):
        prize.append(100 * (10 + diceCount_2[2][0]))
    else:
        prize.append(max(diceCount_2[1]) * 100)

print(max(prize))