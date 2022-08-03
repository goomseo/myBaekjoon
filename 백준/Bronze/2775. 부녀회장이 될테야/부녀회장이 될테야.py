import sys
input = sys.stdin.readline

def countMembers():
    floors, roomNum = (int(input()) for _ in range(2))
    
    rooms = [[0 for _ in range(roomNum)] for _ in range(floors + 1)]
    rooms[0] = list(range(1, (roomNum + 1)))

    for idx1 in range(1, len(rooms)):
        for idx2 in range(roomNum):
            rooms[idx1][idx2] = sum(rooms[idx1-1][:(idx2 + 1)])

    return rooms[-1][-1]


[print(countMembers()) for _ in range(int(input()))]