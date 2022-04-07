strInputs = []
while True:
    strInput = input()
    if strInput == '0':
        break
    strInputs.append(strInput)

for original in strInputs:
    numReversed = list(original)
    numReversed.reverse()
    reversed = ''.join(numReversed)

    if original == reversed:
        print('yes')
    else:
        print('no')