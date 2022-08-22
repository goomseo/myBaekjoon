import sys
input = sys.stdin.readline

input()
seatNums = []
rejectedPeople = 0

for seatNum in list(map(int, input().rstrip().split())):
    if seatNum not in seatNums:
        seatNums.append(seatNum)
    else:
        rejectedPeople += 1

print(rejectedPeople)