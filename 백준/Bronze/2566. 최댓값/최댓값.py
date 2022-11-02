import sys
input = sys.stdin.readline

dictionary = {}
for i in range(9):
    nums = tuple(map(int, input().rstrip().split()))

    j = 0
    for num in nums:
        coordinate = (i, j)
        dictionary[num] = coordinate
        j += 1

        if j == 9:
            break

maximum = max(dictionary.keys())
print(maximum)

row, column = dictionary[maximum]
print(row + 1, column + 1)