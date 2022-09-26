import sys
input = sys.stdin.readline

nums = []
for _ in range(3):
    for _ in range(int(input())):
        nums.append(int(input()))
    
    total = sum(nums)

    if total > 0:
        print('+')
    elif total < 0:
        print('-')
    else:
        print(0)
    
    nums.clear()