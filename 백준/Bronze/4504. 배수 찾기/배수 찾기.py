import sys
input = sys.stdin.readline

N = int(input())

testCases = []
while True:
    num = int(input())

    if not num:
        break

    testCases.append(num)

[print(f'{testCase} is NOT a multiple of {N}.' if testCase % N else f'{testCase} is a multiple of {N}.') for testCase in testCases]