import random
import sys
input = sys.stdin.readline

heights = [int(input()) for _ in range(9)]

total = []
idx_fixed = 10
while True:
    while len(total) != 7:
        idx = random.randint(0, (len(heights) - 1))
        
        if heights[idx] in total:
            continue
        else:
            total.append(heights[idx])

    if sum(total) == 100:
        break

    total.clear()

[print(height) for height in sorted(total)]