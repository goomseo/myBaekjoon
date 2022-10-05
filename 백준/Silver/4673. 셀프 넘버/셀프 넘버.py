def d(num):
    totalOfEachDigit = 0
    i = num
    while i != 0:
        totalOfEachDigit += i % 10
        i //= 10
        
    return num + totalOfEachDigit

notSelfNumList = []
for num in range(1, 10001):
    notSelfNumList.append(d(num))

for number in range(1, 10001):
    if number not in notSelfNumList:
        print(number)