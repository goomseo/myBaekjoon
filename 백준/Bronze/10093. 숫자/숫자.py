import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

if A > B:
    A , B = B, A

if A == B:
    print(0)
    print('')
    exit()

print(B - A - 1)

between = [str(num) for num in range((A + 1), B)]
print(' '.join(between))