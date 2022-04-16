numList = list(input().split())
cmpNumList = sorted(numList)

if numList == cmpNumList:
    print('ascending')
else:
    cmpNumList.reverse()

    if numList == cmpNumList:
        print('descending')
    else:
        print('mixed')