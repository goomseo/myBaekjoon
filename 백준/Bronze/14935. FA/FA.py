def func(x):
    global X
    y = int(x[0]) * len(x)
    if int(x) == y:
        return 'FA'
    elif y == X:
        return 'NFA'
    else:
        return func(str(y))

X = input()
print(func(X))