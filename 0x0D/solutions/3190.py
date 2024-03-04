from collections import deque

n = int(input())  # 보드판
k = int(input())  # 사과 개수

board = [[0 for _ in range(n)] for _ in range(n)]
route = [False for _ in range(10001)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

l = int(input())  # 이동 경로
for _ in range(l):
    t, d = input().split()
    route[int(t)] = d

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

queue = deque()
queue.append((0, 0))  # x좌표, y 좌표, direction (상0, 우1, 하2, 좌3)
time = 0

d = 1
while queue:
    time += 1  # 매 초마다 움직임

    pos = queue[0]
    x, y = pos[0] + direction[d][0], pos[1] + direction[d][1]
    if (x, y) in queue:
        break
    queue.appendleft((x, y))

    if not 0 <= x < n or not 0 <= y < n:
        break
    if board[x][y] == 1:
        board[x][y] = 0
    elif board[x][y] == 0:
        queue.pop()
    if route[time]:
        flag = 1
        if route[time] == 'L':  # 반시계 방향
            flag = -1
        d = (4 + flag + d) % 4

print(time)