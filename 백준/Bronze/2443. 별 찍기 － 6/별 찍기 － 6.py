N = 2 * int(input()) - 1
for i in range(N, 0, -2):
    print(' ' * ((N - i) // 2), end = '')
    print('*' * i)