import sys

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))


def robot(x, y, d, cnt):
    '''
    상하좌우의 값 중 0을 방향 순서대로 찾음
    방향은 반 시계 방향으로 진행 0 -> 3 -> 2 -> 1 ->
    상하좌우의 값 중 0이 없을 때 현재 방향 뒤의 값이 벽(1)이 아니면 후진 가능, 벽이라면 break

    :param x: 좌표 x
    :param y: 좌표 y
    :param d: 방향
    :param cnt: 좌표의 값이 1이 아니고 방문하지 않았을 때
    :return: cnt의 개수
    '''
    if board[x][y] == 0:
        board[x][y] = 2  # 벽이 무조건 1이기 때문에 방문한 것 2로 변경
        cnt += 1

    flag = True
    for i in range(1, 5):
        pos = (4 - i + d) % 4

        if pos == 0 and board[x - 1][y] == 0:
            cnt = robot(x - 1, y, pos, cnt)
            flag = False
            break
        elif pos == 1 and board[x][y + 1] == 0:
            cnt = robot(x, y + 1, pos, cnt)
            flag = False
            break
        elif pos == 2 and board[x + 1][y] == 0:
            cnt = robot(x + 1, y, pos, cnt)
            flag = False
            break
        elif pos == 3 and board[x][y - 1] == 0:
            cnt = robot(x, y - 1, pos, cnt)
            flag = False
            break
    if flag:  # 상하좌우에 방문할 곳 없을 때 후진 가능한 지 확인, [!] 벽 아니면 후진 가능함
        if d == 0 and board[x+1][y] != 1:
            cnt = robot(x + 1, y, d, cnt)
        elif d == 1 and board[x][y-1] != 1:
            cnt = robot(x, y - 1, d, cnt)
        elif d == 2 and board[x-1][y] != 1:
            cnt = robot(x - 1, y, d, cnt)
        elif d == 3 and board[x][y+1] != 1:
            cnt = robot(x, y + 1, d, cnt)

    return cnt


print(robot(r, c, d, 0))
