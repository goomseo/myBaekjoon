import sys
input = sys.stdin.readline

def operation(a, operator, b):
    if operator == '>':
        if a > b:
            return True
        else:
            return False
    elif operator == '>=':
        if a >= b:
            return True
        else:
            return False
    elif operator == '<':
        if a < b:
            return True
        else:
            return False
    elif operator == '<=':
        if a <= b:
            return True
        else:
            return False
    elif operator == '==':
        if a == b:
            return True
        else:
            return False
    else:
        if a != b:
            return True
        else:
            return False

idx = 1
while True:
    a, operator, b = input().rstrip().split()

    if operator == 'E':
        break

    print(f'Case {idx}: true' if operation(int(a), operator, int(b)) else f'Case {idx}: false')
    idx += 1
