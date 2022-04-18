import sys
input = sys.stdin.readline

word = input().upper().rstrip()

cmpList =[]
for i in word:
    if i not in cmpList:
        cmpList.append(i)

countList= []
for j in range(len(cmpList)):
    countList.append(word.count(cmpList[j]))

mostUsedChar = max(countList)
if countList.count(mostUsedChar) > 1:
    print('?')
else:
    idx = countList.index(mostUsedChar)
    print(cmpList[idx])