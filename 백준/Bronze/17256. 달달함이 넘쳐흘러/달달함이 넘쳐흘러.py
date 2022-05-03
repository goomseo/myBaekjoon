import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
c = list(map(int, input().split()))

print(f'{c[0] - a[2]} {int(c[1] / a[1])} {c[2] - a[0]}')