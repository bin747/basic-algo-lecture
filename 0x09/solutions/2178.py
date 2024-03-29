import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

board = []
queue = deque()
max_size = -1

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

d = ((0, -1), (-1, 0), (0, 1), (1, 0))

queue.append((0, 0))
while queue:
    pos = queue.popleft()
    for dx, dy in d:
        x, y = pos[0] + dx, pos[1] + dy

        if (not 0 <= x < n) or (not 0 <= y < m):
            continue

        if not board[x][y]:
            continue
        if board[x][y] == 1:
            queue.append((x, y))
            board[x][y] = board[pos[0]][pos[1]] + 1

print(board[n-1][m-1])