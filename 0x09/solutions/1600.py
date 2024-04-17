from collections import deque

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d2 = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
queue = deque()
board = []

k = int(input())
w, h = map(int, input().split())

vis = [[[(0, 0) for _ in range(k+1)] for _ in range(w)] for _ in range(h)]  # vis[i][j][k] = 방문, 카운트

for _ in range(h):
    board.append(list(map(int, input().split())))

queue.append((0, 0, 0))    # i, j, k
vis[0][0][0] = (1, 0)

while queue:
    pos = queue.popleft()

    # 원숭이로 이동
    for dx, dy in d:
        x, y = pos[0] + dx, pos[1] + dy

        if not 0 <= x < h or not 0 <= y < w:
            continue

        if not board[x][y] and not vis[x][y][pos[2]][0]:
            queue.append((x, y, pos[2]))
            vis[x][y][pos[2]] = (1, vis[pos[0]][pos[1]][pos[2]][1] + 1)

    # 말처럼 이동
    if pos[2] < k:
        for dx, dy in d2:
            x, y = pos[0] + dx, pos[1] + dy

            if not 0 <= x < h or not 0 <= y < w:
                continue

            if not board[x][y] and not vis[x][y][pos[2] + 1][0]:
                queue.append((x, y, pos[2] +  1))
                vis[x][y][pos[2]+1] = (1, vis[pos[0]][pos[1]][pos[2]][1] + 1)

isVis = False
minCnt = -1
for i in range(k + 1):
    if vis[h - 1][w - 1][i][0] > 0:
        isVis = True
        minCnt = vis[h - 1][w - 1][i][1] if minCnt == -1 else min(minCnt, vis[h - 1][w - 1][i][1])
print(minCnt)