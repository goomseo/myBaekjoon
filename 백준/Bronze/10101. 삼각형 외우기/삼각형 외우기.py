angles = [int(input()) for _ in range(3)]

if sum(angles) != 180:
    print('Error')
else:
    count = 0
    for idx1, idx2 in ((0, 1), (0, 2), (1, 2)):
        if angles[idx1] == angles[idx2]:
            count += 1

    if count == 3:
        print('Equilateral')
    elif count == 1:
        print('Isosceles')
    else:
        print('Scalene')