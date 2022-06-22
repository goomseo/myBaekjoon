import sys
input = sys.stdin.readline

participations = dict(zip(('Soongsil', 'Korea', 'Hanyang'), (map(int, input().rstrip().split()))))

if sum(participations.values()) >= 100:
    print('OK')
else:
    items = tuple(participations.items())
    leastParticipation = min(items[0][1], items[1][1], items[2][1])

    for item in items:
        if leastParticipation in item:
            print(item[0])