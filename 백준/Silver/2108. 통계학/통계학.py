import statistics as stats
from collections import Counter
import sys
input = sys.stdin.readline

def getMode(num_list):
    num_list.sort()
    modes = Counter(num_list).most_common()

    if len(modes) > 1:
        if modes[0][1] == modes[1][1]:
            return modes[1][0]
        else:
            return modes[0][0]
    else:
        return modes[0][0]

num_list = [int(input()) for _ in range(int(input()))]

print(round(stats.mean(num_list)))
print(stats.median(num_list))
print(getMode(num_list))
print(max(num_list) - min(num_list))