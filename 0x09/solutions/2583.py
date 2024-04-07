queue = []
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cntList = []

m, n, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    # sample = list(map(int, input().split()))
    # sx, sy, ex, ey = m - sample[1], sample[0], m - sample[3], sample[2] # 왼쪽 위가 0, 0인 좌표로 변경
    sx, sy, ex, ey = map(int, input().split())
    # 왼쪽 아래부터 입력받았기 때문에 무조건 sx가 ex보다 큼
    for i in range(sy, ey):
        for j in range(sx, ex):
            if not board[i][j]:
                board[i][j] = 1
for i in range(m):
    for j in range(n):
        if not board[i][j]:
            board[i][j] = 1
            queue.append((i, j))
            cnt = 1

            while queue:
                pos = queue.pop()
                for dx, dy in d:
                    x, y = pos[0] + dx, pos[1] + dy

                    if not 0 <= x < m or not 0 <= y < n:
                        continue
                    if not board[x][y]:
                        queue.append((x, y))
                        board[x][y] = 1
                        cnt += 1
            cntList.append(cnt)

print(len(cntList))
print(*sorted(cntList))