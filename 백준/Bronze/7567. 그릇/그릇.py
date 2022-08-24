import sys
input = sys.stdin.readline

dishes = input().rstrip()
height = 10

for idx in range(len(dishes) - 1):
    if dishes[idx] == dishes[idx+1]:
        height += 5
    else:
        height += 10

print(height)