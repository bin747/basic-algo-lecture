n = int(input())
board = []
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

maxCnt = 0
for _ in range(n):
    sample = list(map(int, input().split()))
    maxCnt = max(maxCnt, max(sample))
    board.append(sample)
result = [-1 for _ in range(maxCnt + 1)]


def safe(flag, board):
    cnt = 0
    queue = []
    vis = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > flag and not vis[i][j]:
                queue.append((i, j))
                vis[i][j] = True
                cnt += 1

                while queue:
                    pos = queue.pop()

                    for dx, dy in d:
                        x, y = pos[0] + dx, pos[1] + dy

                        if not 0 <= x < n or not 0 <= y < n:
                            continue

                        if board[x][y] > flag and not vis[x][y]:
                            queue.append((x, y))
                            vis[x][y] = True

    return cnt


for i in range(maxCnt + 1):
    result[i] = safe(i, board)

print(max(result))
