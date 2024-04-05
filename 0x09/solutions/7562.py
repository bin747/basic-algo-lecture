from collections import deque
t = int(input())

d = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (2, 1), (1, 2)]
for _ in range(t):
    l = int(input())
    board = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque()
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    queue.append((sx, sy))
    board[sx][sy] = 1
    while queue:
        pos = queue.popleft()
        for dx, dy in d:
            x, y = pos[0] + dx, pos[1] + dy
            if not 0 <= x < l or not 0 <= y < l:
                continue

            if board[x][y] == 0 or board[x][y] > board[pos[0]][pos[1]] + 1:
                board[x][y] = board[pos[0]][pos[1]] + 1
                queue.append((x, y))
                if x == ex and y == ey:
                    queue.clear()
                    break
    print(board[ex][ey] - 1)
