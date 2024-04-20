from collections import deque

n, m = map(int, input().split())

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visit = [[[0, 0] for _ in range(n)] for _ in range(n)]  # 불 켜짐 여부, 방문 여부
board = [[[] for _ in range(n)] for _ in range(n)]
queue = deque()

for _ in range(m):
    x, y, a, b = map(int, input().split())
    board[x - 1][y - 1].append((a - 1, b - 1))

visit[0][0] = [1, 1]
queue.append((0, 0))
cnt = 1

while queue:
    posX, posY = queue.popleft()

    while board[posX][posY]:
        switchX, switchY = board[posX][posY].pop()

        if not 0 <= switchX < n or not 0 <= switchY < n:
            continue
        if switchX == posX and switchY == posY:
            continue
        if not visit[switchX][switchY][0]:  # 불이 꺼져 있다면
            visit[switchX][switchY][0] = 1  # 켜주고
            cnt += 1

            for dx, dy in d:  # 해당 지점 방문할 수 있는 지 확인
                x, y = switchX + dx, switchY + dy

                if not 0 <= x < n or not 0 <= y < n:
                    continue

                if visit[x][y][1]:  # 주변이 방문한 적 있다 -> 나도 방문할 수 있다
                    visit[switchX][switchY][1] = 1  # 방문 처리 후
                    queue.append((switchX, switchY))  # 큐 추가
                    break

    for dx, dy in d:
        x, y = posX + dx, posY + dy

        if not 0 <= x < n or not 0 <= y < n:
            continue

        if visit[x][y][0] and not visit[x][y][1]:  # 불 켜져 있고 방문 하지 않았을 때 -> 방문 처리 및 큐 추가
            visit[x][y][1] = 1
            queue.append((x, y))

print(cnt)
