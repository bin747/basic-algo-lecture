test = int(input())

d = ((1, 0), (0, 1), (-1, 0), (0, -1))
for _ in range(test):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1
    queue = []
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] <= 0:
                continue
            queue.append((i, j))
            count += 1
            board[i][j] = -1
            while queue:
                pos = queue.pop()
                for dx, dy in d:
                    x, y = pos[0] + dx, pos[1] + dy

                    if not 0 <= x < n or not 0 <= y < m:
                        continue

                    if board[x][y] == 1:
                        queue.append((x, y))
                        board[x][y] = -1
    print(count)
