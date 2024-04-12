from collections import deque

n, m = map(int, input().split())

vis = [[(False, False, -1) for _ in range(m)] for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque()
board = []

for _ in range(n):
    board.append(list(map(int, input())))

queue.append((0, 0))
board[0][0] = 1
vis[0][0] = (True, False, 1)  # 방문, 벽뚫, 개수

while queue:
    pos = queue.popleft()
    for dx, dy in d:
        x, y = pos[0] + dx, pos[1] + dy

        if not 0 <= x < n or not 0 <= y < m:
            continue

        if not board[x][y]:  # 벽이 아닐 때
            if vis[x][y][1] and not vis[pos[0]][pos[1]][1] or not vis[x][y][0]:  # 가려고 하는 곳 벽뚫, 난 벽뚫 x || 방문 x
                vis[x][y] = (True, vis[pos[0]][pos[1]][1], vis[pos[0]][pos[1]][2] + 1)
                queue.append((x, y))
        else:  # 벽일 때
            if not vis[pos[0]][pos[1]][1] and not vis[x][y][0]:  # 벽뚫 사용 안 했으면
                vis[x][y] = (True, True, vis[pos[0]][pos[1]][2] + 1)
                queue.append((x, y))
        if x == n-1 and y == m-1:
            print(vis[n - 1][m - 1][2])
            quit()
print(-1 if not vis[n-1][m-1][0] else vis[n-1][m-1][2])