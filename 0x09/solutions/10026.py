n = int(input())
board = []
notVis = [[0 for _ in range(n)] for _ in range(n)]
vis = [[0 for _ in range(n)] for _ in range(n)]
notQueue = []
queue = []
cnt = 0
notCnt = 0
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    board.append(list(input()))
for i in range(n):
    for j in range(n):
        if not queue and not vis[i][j]:
            queue.append((i, j))
            vis[i][j] = 1
            cnt += 1
            while queue:
                pos = queue.pop()
                for dx, dy in d:
                    x, y = pos[0] + dx, pos[1] + dy
                    if not 0 <= x < n or not 0 <= y < n:
                        continue
                    if not vis[x][y]:
                        if board[x][y] != board[pos[0]][pos[1]]:
                            if board[x][y] == 'B' or board[pos[0]][pos[1]] == 'B':
                                continue
                        queue.append((x, y))
                        vis[x][y] = 1
        if not notQueue and not notVis[i][j]:
            notQueue.append((i, j))
            notVis[i][j] = 1
            notCnt += 1
            while notQueue:
                pos = notQueue.pop()
                for dx, dy in d:
                    x, y = pos[0] + dx, pos[1] + dy
                    if not 0 <= x < n or not 0 <= y < n:
                        continue
                    if board[x][y] == board[pos[0]][pos[1]] and not notVis[x][y]:
                        notQueue.append((x, y))
                        notVis[x][y] = 1

print(notCnt, cnt, end=' ')

