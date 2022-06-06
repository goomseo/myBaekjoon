import sys
input = sys.stdin.readline

def countZero(start, end):
    nums = [str(num) for num in range(start, (end + 1)) if str(num).count('0')]

    cnt = 0
    for num in nums:
        cnt += num.count('0')

    return cnt

def main():
    rpt = int(input().rstrip())

    for _ in range(rpt):
        start, end = map(int, input().rstrip().split())
        print(countZero(start, end))

main()