from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())

decreasingNum_list = []
for i in range(1, 11):
    for combination in combinations(range(10), i):
        decreasingNum_list.append(int(''.join(sorted(map(str, combination), reverse = True))))
        decreasingNum_list.sort()

try:    
    print(decreasingNum_list[N])
except:
    print(-1)