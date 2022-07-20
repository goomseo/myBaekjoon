A, B = map(int, input().split())
arr = [0 for _ in range(B)]

i = 1
cnt = 0
for idx in range(B):
    arr[idx] = i
    cnt += 1

    if i == cnt:
        i += 1
        cnt = 0

print(sum(arr[(A - 1):(B + 1)]))