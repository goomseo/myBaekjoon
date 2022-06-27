import sys
input = sys.stdin.readline

x_y = [[], []]
for x, y in [input().rstrip().split() for _ in range(3)]:
    x_y[0].append(x)
    x_y[1].append(y)

coordinate = []
for values in x_y:
    values.sort()
    for value in values:
        if values[1] != value:
            coordinate.append(value)
            break

print(' '.join(coordinate))