import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [n for n in range(1, (N + 1))]

answer = []
while len(answer) != N:
    length = len(arr)
    while len(arr) < K:
        arr += arr
    
    answer.append(str(arr[K-1]))

    if length != len(arr):
        arr = arr[:length]
        arr = arr[arr.index(int(answer[-1])) + 1:] + arr[:arr.index(int(answer[-1]))]
        continue
    
    arr = arr[K:] + arr[:(K-1)]

print('<' + ', '.join(answer) + '>')