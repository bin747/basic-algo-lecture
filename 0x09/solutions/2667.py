from collections import deque

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
queue = deque()
board = []
cntList = []

n = int(input())
for _ in range(n):
    board.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            queue.append((i, j))
            board[i][j] = -1
            cnt = 1

            while queue:
                pos = queue.popleft()

                for dx, dy in d:
                    x, y = pos[0] + dx, pos[1] + dy

                    if not 0 <= x < n or not 0 <= y < n:
                        continue

                    if board[x][y] == 1:
                        board[x][y] = -1
                        queue.append((x, y))
                        cnt += 1

            cntList.append(cnt)

print(len(cntList))
print(*sorted(cntList), sep='\n')