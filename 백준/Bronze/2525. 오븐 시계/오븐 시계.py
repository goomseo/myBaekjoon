hr, min = map(int, input().split())
ovenTime = int(input())

endTime = (hr * 60) + min + ovenTime

if endTime >= 1440:
    endTime -= 1440
    print(f'{endTime // 60} {endTime % 60}')
else:
    print(f'{endTime // 60} {endTime % 60}')