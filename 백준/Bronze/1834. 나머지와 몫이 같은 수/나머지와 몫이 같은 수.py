N = int(input())

total = 0
q = 1
while q < N:
    total += (q * (N + 1))
    q += 1

print(total)