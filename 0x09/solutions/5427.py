from collections import deque

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    queue = deque()
    board = []
    for i in range(h):
        sample = list(input())
        px, py = -1, -1
        for j in range(w):
            if sample[j] == '@':
                queue.append((i, j))
                px, py = i, j
            if sample[j] == '*':
                queue.appendleft((i, j))

        board.append(sample)
        if py != -1:
            board[i][py] = 1
    while queue:
        pos = queue.popleft()

        for dx, dy in d:
            x, y = pos[0] + dx, pos[1] + dy

            if not 0 <= x < h or not 0 <= y < w:
                if board[pos[0]][pos[1]] == '*':
                    continue
                else:
                    px, py = pos[0], pos[1]
                    queue.clear()
                    break

            if board[x][y] == '.':
                if board[pos[0]][pos[1]] == '*':
                    board[x][y] = '*'
                    queue.append((x, y))
                else:
                    board[x][y] = board[pos[0]][pos[1]] + 1
                    queue.append((x, y))
                    px, py = x, y
    if px == h - 1 or px == 0 or py == w - 1 or py == 0:
        print(board[px][py])
    else:
        print('IMPOSSIBLE')
