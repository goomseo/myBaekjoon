import sys
input = sys.stdin.readline

for _ in range(int(input())):
    H, W, N = map(int, input().rstrip().split())

    rooms = []
    for j in range(1, (W + 1)):
        for i in range(1, (H + 1)):
            rooms.append([str(i), str(j)])

    roomNum = rooms[N - 1]
    if (len(roomNum[0]) > len(roomNum[1])) or (len(''.join(rooms[N - 1])) == 2):
        roomNum = '0'.join(roomNum)

    print(''.join(roomNum))