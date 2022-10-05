import sys
input = sys.stdin.readline

N = int(input())

generators = []
for generator in range(1, N):
    if generator + sum(list(map(int, (str(generator))))) == N:
        generators.append(generator)
        break

print(generators[0] if len(generators) else 0)