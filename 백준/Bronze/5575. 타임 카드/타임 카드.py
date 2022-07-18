import sys
input = sys.stdin.readline

def timecode(string):
    times = list(map(int, string.split()))
    start_end = []

    for time in (times[:3], times[3:]):
        start_end.append(time[0] * 3600 + time[1] * 60 + time[2])

    workedTime = start_end[1] - start_end[0]

    print(workedTime // 3600, end = ' ')
    workedTime %= 3600
    print(workedTime // 60, end = ' ')
    workedTime %= 60
    print(workedTime)

for _ in range(3):
    timecode(input())