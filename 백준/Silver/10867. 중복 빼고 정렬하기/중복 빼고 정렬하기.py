input()
[print(num, end = ' ') for num in sorted(list(set(map(int, input().split()))))]