date = int(input())
carNums = map(int, input().split())

count = 0
for carNum in carNums:
    if carNum == date:
        count += 1

print(count)