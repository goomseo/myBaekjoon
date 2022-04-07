num = int(input())
new_num = ''
cnt_cycle = 0

# 새로운 수 구하는 함수
def find_new_num(number):
    tens = number % 10
    units = sum(divmod(number, 10)) % 10
    return tens * 10 + units

# 사이클
new_num = find_new_num(num)
while new_num != num:
    new_num = find_new_num(new_num)
    cnt_cycle += 1

# 사이클 길이 출력
print(cnt_cycle + 1)