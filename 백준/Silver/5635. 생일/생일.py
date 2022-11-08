import sys
input = sys.stdin.readline

birthdate_name = {}
for _ in range(int(input())):
    name, day, month, year = input().rstrip().split()

    birthdate = tuple(map(int, (year, month, day)))
    birthdate_name[birthdate] = name

birthdate_list = list(birthdate_name.keys())

print(birthdate_name[max(birthdate_list)])
print(birthdate_name[min(birthdate_list)])