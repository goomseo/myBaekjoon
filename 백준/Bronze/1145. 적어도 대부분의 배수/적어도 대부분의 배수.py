import sys
input = sys.stdin.readline

nums = list(map(int, input().rstrip().split()))
multiple = 1

counts = 0
while True:
    for num in nums:
        if not(multiple % num):
            counts += 1

    if counts >= 3:
        print(multiple)
        break
    else:
        multiple += 1
        counts = 0