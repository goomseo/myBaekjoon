import sys
input = sys.stdin.readline

def marsMath(num, operators):
    for operator in operators:
        if operator == '@':
            num *= 3
        elif operator == '%':
            num += 5
        else:
            num -= 7
    
    return num

def main():
    for _ in range(int(input())):
        num, *(operators) = input().rstrip().split()
        print(f'{marsMath(float(num), operators):.2f}')

main()