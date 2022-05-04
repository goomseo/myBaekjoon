import sys
input = sys.stdin.readline

def hansoo(num):
    digits = list(str(num))
    if (int(digits[0]) + int(digits[2])) == int(digits[1]) * 2:
        return True
    else:
        return False

def main():
    n = int(input())

    if n < 100:
        print(n)
    else:
        cnt = 99
        for i in range(100, n + 1):
            if hansoo(i) == True:
                cnt += 1
        
        print(cnt)

main()