nums = input().split()

temp = ''
numsReversed = []
for i in range(2):
    for j in range(3):
        temp = nums[i][j] + temp
    numsReversed.append(temp)
    temp = ''

print(max(numsReversed))