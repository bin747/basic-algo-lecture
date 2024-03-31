from collections import deque

d = ((1, 0), (0, 1), (-1, 0), (0, -1))
queue = deque()
cnt = 1
n, m = map(int, input().split())
board = []

for i in range(n):
    status = list(input())
    y = -1
    for j in range(m):
        if status[j] == 'J':
            queue.append((i, j))
            px = i
            py = j
            y = j
        if status[j] == 'F':
            queue.appendleft((i, j))
    board.append(status)
    if y != -1:
        board[i][y] = 1

while queue:
    pos = queue.popleft()
    for dx, dy in d:
        x, y = pos[0] + dx, pos[1] + dy

        if not 0 <= x < n or not 0 <= y < m:
            continue

        if px == 0 or px == n - 1 or py == 0 or py == m - 1:
            break
        if board[x][y] == '.':
            if board[pos[0]][pos[1]] == 'F':
                board[x][y] = 'F'
                queue.append((x, y))
            else:
                board[x][y] = board[pos[0]][pos[1]] + 1
                cnt = board[x][y]
                px = x
                py = y

                queue.append((x, y))

if not (px == 0 or px == n-1) and not (py == 0 or py == m-1):
    print('IMPOSSIBLE')
else:
    print(cnt)
