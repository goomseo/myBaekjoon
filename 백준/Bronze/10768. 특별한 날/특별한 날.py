import sys
input = sys.stdin.readline

month, day = [int(input()) for _ in range(2)]

if month < 2:
    print('Before')
elif month > 2:
    print('After')
elif day < 18:
    print('Before')
elif day > 18:
    print('After')
else:
    print('Special')