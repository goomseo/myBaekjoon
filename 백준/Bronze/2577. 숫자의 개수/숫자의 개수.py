import sys

data = [int(sys.stdin.readline()) for i in range(3)]
multiply = list(str(data[0] * data[1] * data[2]))

for j in range(10):
    qtyNum = multiply.count(str(j))
    print(qtyNum)