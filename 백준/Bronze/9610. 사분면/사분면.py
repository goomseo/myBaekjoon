import sys
input = sys.stdin.readline

location_dict = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0, 'AXIS': 0}
for _ in range(int(input())):
    x, y = map(int, input().rstrip().split())

    if x > 0 and y > 0:
        location_dict['Q1'] += 1
    elif x < 0 and y > 0:
        location_dict['Q2'] += 1
    elif x < 0 and y < 0:
        location_dict['Q3'] += 1
    elif x > 0 and y < 0:
        location_dict['Q4'] += 1
    else:
        location_dict['AXIS'] += 1

[print(f'{key}: {value}') for key, value in location_dict.items()]