hr, min = map(int, input().split())

x = (hr * 60 + min) - 45

if x < 0:
    x += 1440
    newHrA = x // 60
    newMinA = x % 60
    print(newHrA, newMinA)
else:
    newHrB = x // 60
    newMinB = x % 60
    print(newHrB, newMinB)