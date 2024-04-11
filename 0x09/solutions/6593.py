from collections import deque

d = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]
while True:
    l, r, c = map(int, input().split())
    if not l and not r and not c:
        break
    eh, ex, ey = -1, -1, -1
    board = []
    queue = deque()
    for h in range(l):
        sample = []
        for x in range(r):
            status = list(input())
            for y in range(c):
                if status[y] == 'S':
                    queue.append((h, x, y))
                    status[y] = 0
                if status[y] == 'E':
                    eh, ex, ey = h, x, y
            sample.append(status)
        board.append(sample)
        input()

    while queue:
        pos = queue.popleft()

        for dh, dx, dy in d:
            h, x, y = pos[0] + dh, pos[1] + dx, pos[2] + dy

            if not 0 <= h < l or not 0 <= x < r or not 0 <= y < c:
                continue

            if board[h][x][y] == '.':
                board[h][x][y] = board[pos[0]][pos[1]][pos[2]] + 1
                queue.append((h, x, y))
            if board[h][x][y] == 'E':
                board[h][x][y] = board[pos[0]][pos[1]][pos[2]] + 1
                queue.clear()
                break

    if board[eh][ex][ey] == 'E':
        print('Trapped!')
    else:
        print('Escaped in {0} minute(s).'.format(board[eh][ex][ey]))
