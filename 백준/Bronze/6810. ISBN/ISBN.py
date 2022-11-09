import sys
input = sys.stdin.readline

isbn = "9780921418"
for _ in range(3):
    isbn += input().rstrip()

one_three_sum = 0
for idx in range(len(isbn)):
    if idx % 2:
        one_three_sum += int(isbn[idx]) * 3
    else:
        one_three_sum += int(isbn[idx])

print("The 1-3-sum is", one_three_sum)