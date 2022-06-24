import sys
input = sys.stdin.readline

patient, doctor = [len(input().rstrip()) for _ in range(2)]

print('go' if patient >= doctor else 'no')