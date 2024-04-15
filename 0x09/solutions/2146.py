from collections import deque
import sys

n = int(input())

board = []
vis = [[False for _ in range(n)] for _ in range(n)]
queue = deque()
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

# 섬에 번호 입력
num = 0
for i in range(n):
    for j in range(n):
        if not vis[i][j] and board[i][j] == 1:
            num += 1
            queue.append((i, j))
            board[i][j] = num
            vis[i][j] = True

            while queue:
                pos = queue.pop()

                for dx, dy in d:
                    x, y = pos[0] + dx, pos[1] + dy

                    if not 0 <= x < n or not 0 <= y < n:
                        continue

                    if not vis[x][y] and board[x][y] == 1:
                        queue.append((x, y))
                        vis[x][y] = True
                        board[x][y] = num

vis = [[(False, 0, 0) for _ in range(n)] for _ in range(n)]

# 섬 외곽을 먼저 큐에 넣음
for i in range(n):
    for j in range(n):
        if not board[i][j]:  # 섬 외곽 큐에 넣음
            for dx, dy in d:
                x, y = i + dx, j + dy

                if not 0 <= x < n or not 0 <= y < n:
                    continue

                if board[x][y] > 0:  # 주변이 섬일 때
                    if not vis[i][j][0]:  # 현재 위치가 방문하지 않았으면
                        queue.append((i, j))
                        vis[i][j] = (True, board[x][y], 1)  # 방문, 섬 넘버, 다리 개수
                    elif vis[i][j][1] != board[x][y]:  # 현재 위치가 방문한 것 == 인접한 섬이 2개인지 체크 == 다리 1개 바로 끝
                        print(1)
                        quit()
minLength = 5000  # 총 100까지라고 했으니 최대 값 임의로 설정
while queue:  # 외곽부터 시작
    pos = queue.popleft()

    for dx, dy in d:
        x, y = pos[0] + dx, pos[1] + dy

        if not 0 <= x < n or not 0 <= y < n:
            continue

        if not board[x][y]:  # 바다면서
            if not vis[x][y][0]:  # 방문하지 않았으면
                vis[x][y] = (True, vis[pos[0]][pos[1]][1], vis[pos[0]][pos[1]][2] + 1)  # 방문, 섬 넘버, 다리 개수
                queue.append((x, y))
            else:  # 방문 한 거면
                if vis[x][y][1] != vis[pos[0]][pos[1]][1]:  # 섬 넘버 확인
                    minLength = min(minLength, vis[x][y][2] + vis[pos[0]][pos[1]][2])  # 최소값 확인
print(minLength)
