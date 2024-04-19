from collections import deque

n, m, k = map(int, input().split())

vis = [[(0, 0, -1) for _ in range(m)] for _ in range(n)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque()
board = []

for _ in range(n):
    board.append(list(map(int, input())))

queue.append((0, 0))
board[0][0] = 1
vis[0][0] = (1, 0, 1)  # 방문, 벽뚫 횟수, 개수

while queue:
    pos = queue.popleft()
    for dx, dy in d:
        x, y = pos[0] + dx, pos[1] + dy

        if not 0 <= x < n or not 0 <= y < m:
            continue

        if not board[x][y]:  # 벽이 아닐 때
            # 내 벽뚫 횟수 < 가려고 하는 곳 벽뚫 횟수 || 방문 x
            if vis[pos[0]][pos[1]][1] < vis[x][y][1] or not vis[x][y][0]:
                vis[x][y] = (1, vis[pos[0]][pos[1]][1], vis[pos[0]][pos[1]][2] + 1)
                queue.append((x, y))
        else:  # 벽일 때
            # 내 벽뚫 횟수 < 가려고 하는 곳 벽뚫 횟수 || 내 벽뚫 횟수 < k && 방문 x
            if vis[pos[0]][pos[1]][1] < k and not vis[x][y][0] or vis[pos[0]][pos[1]][1] + 1 < vis[x][y][1]:
                vis[x][y] = (1, vis[pos[0]][pos[1]][1] + 1, vis[pos[0]][pos[1]][2] + 1)
                queue.append((x, y))
        if x == n - 1 and y == m - 1:
            print(vis[n - 1][m - 1][2])
            quit()
print(-1 if not vis[n - 1][m - 1][0] else vis[n - 1][m - 1][2])