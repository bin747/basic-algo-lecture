from collections import deque

d = ((-1, 0 , 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1))

m, n, h = map(int, input().split())
board = []
queue = deque()
cnt = 0
day = 0
for i in range(h):
    sample = []
    for j in range(n):
        status = list(map(int, input().split()))
        for k in range(m):
            if status[k] == 1:
                queue.append((i, j, k))
        cnt += status.count(0)
        sample.append(status)
    board.append(sample)

if not cnt:
    print(0)
else:
    while queue:
        pos = queue.popleft()

        for dx, dy, dz in d:
            x, y, z = pos[0] + dx, pos[1] + dy, pos[2] + dz

            if not 0 <= x < h or not 0 <= y < n or not 0 <= z < m:
                continue

            if board[x][y][z] == 0:
                queue.append((x, y, z))
                board[x][y][z] = board[pos[0]][pos[1]][pos[2]] + 1
                cnt -= 1
                day = board[x][y][z]

    if not cnt:
        print(day - 1)
    else:
        print(-1)