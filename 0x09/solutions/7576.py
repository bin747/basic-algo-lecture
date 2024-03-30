from collections import deque

m, n = map(int, input().split())

cnt = 0
day = 0
d = ((1, 0), (0, 1), (-1, 0), (0, -1))
board = []
queue = deque()

for i in range(n):
    status = list(map(int, input().split()))
    for j in range(m):
        if status[j] == 1:
            queue.append((i, j))
        if not status[j]:
            cnt += 1
    board.append(status)

if not cnt:
    print(0)
else:
    while queue:
        pos = queue.popleft()
        for dx, dy in d:
            x, y = pos[0] + dx, pos[1] + dy

            if not 0 <= x < n or not 0 <= y < m:
                continue

            if board[x][y] == 0:
                queue.append((x, y))
                board[x][y] = board[pos[0]][pos[1]] + 1
                cnt -= 1
                day = board[x][y]

    if not cnt:
        print(day - 1)
    else:
        print(-1)
