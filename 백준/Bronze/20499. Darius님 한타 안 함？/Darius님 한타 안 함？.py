import sys
input = sys.stdin.readline

K, D, A = map(int, input().rstrip().split('/'))

print('hasu' if (K + A) < D or D == 0 else 'gosu')