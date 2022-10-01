import sys
input = sys.stdin.readline

for _ in range(int(input())):
    drink_dict = {}
    for _ in range(int(input())):
        univName, drink = input().rstrip().split()
        drink_dict[int(drink)] = univName
    
    print(drink_dict[max(drink_dict.keys())])