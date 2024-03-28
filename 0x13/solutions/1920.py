import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

board = [[0 for j in range(m)] for i in range(n)]
vis = [[0 for j in range(m)] for i in range(n)]
queue = []
max_size = 0
count = 0

for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    for j in range(m):
        if not board[i][j] or vis[i][j]:
            continue
        queue.append((i, j))
        vis[i][j] = 1
        count += 1
        size = 0
        while queue:
            size += 1
            x, y = queue.pop()
            if x+1 < n and board[x+1][y] and not vis[x+1][y]:
                queue.append((x+1, y))
                vis[x+1][y] = 1
            if y+1 < m and board[x][y+1] and not vis[x][y+1]:
                queue.append((x, y+1))
                vis[x][y+1] = 1
            if x-1 >= 0 and board[x-1][y] and not vis[x-1][y]:
                queue.append((x-1, y))
                vis[x-1][y] = 1
            if y-1 >= 0 and board[x][y-1] and not vis[x][y-1]:
                queue.append((x, y-1))
                vis[x][y-1] = 1
        max_size = max(max_size, size)

print(count)
print(max_size)