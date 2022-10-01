import sys
input = sys.stdin.readline

def getPrize(dice_list):
    dice_set = set(dice_list)

    if len(dice_set) == 1:
        return 1000 * (10 + dice_list[0])
    elif len(dice_set) == 2:
        for dice in dice_set:
            if dice_list.count(dice) == 2:
                same_dice = dice
                break

        return 100 * (10 + same_dice)
    else:
        return 100 * max(dice_list)

def main():
    prize_list = []
    [prize_list.append(getPrize(list(map(int, input().rstrip().split())))) for _ in range(int(input()))]
    
    print(max(prize_list))

main()