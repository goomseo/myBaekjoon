import sys
input = sys.stdin.readline

pay = 1000 - int(input())

cnt = 0
for change in (500, 100, 50, 10, 5, 1):
    cnt += (pay // change)
    pay %= change

    if not pay:
        break

print(cnt)