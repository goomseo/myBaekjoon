import sys
input = sys.stdin.readline

i = 0
obj_on_white = 0
for _ in range(8):
    line = input().rstrip()

    for idx in range((i % 2), len(line), 2):
        if line[idx] == 'F':
            obj_on_white += 1
    
    i += 1

print(obj_on_white)