cnt_seqnc, criterion = map(int, input().split())
item = list(map(int, input().split()))

for i in range(cnt_seqnc):
    if item[i] < criterion:
        print(item[i], end = ' ')