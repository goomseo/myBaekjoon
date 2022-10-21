import sys
input = sys.stdin.readline

input()
arr = tuple(map(int, input().rstrip().split()))

arr2 = sorted(list(set(arr)))
idxOfNum_dict = {arr2[i] : i for i in range(len(arr2))}

[print(idxOfNum_dict[coordinate], end = ' ') for coordinate in arr]