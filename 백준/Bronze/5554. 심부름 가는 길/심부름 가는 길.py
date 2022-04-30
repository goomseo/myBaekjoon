seconds = [int(input()) for _ in range(4)]
print(f'{sum(seconds) // 60}\n{sum(seconds) % 60}')