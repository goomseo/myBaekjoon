import sys
input = sys.stdin.readline

while True:
    N = int(input())

    if N == -1:
        break
    
    divisor_list = []
    for i in range(1, (N+1)):
        if not N % i:
            divisor_list.append(i)

    if sum(divisor_list) == N * 2:
        print(f'{N} = {" + ".join(map(str, divisor_list[:-1]))}')
    else:
        print(f'{N} is NOT perfect.')