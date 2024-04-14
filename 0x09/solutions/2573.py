from collections import deque

n, m = map(int, input().split())

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = []
queue = deque()
for _ in range(n):
    board.append(list(map(int, input().split())))

year = 0
while True:
    vis = [[False for _ in range(m)] for _ in range(n)]
    flag = True  # if문 조건에 걸리지 않을 때 while문 종료
    landCnt = 0
    year += 1
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if board[i][j] and not vis[i][j]:
                queue.append((i, j))
                vis[i][j] = True
                landCnt += 1  # 조건을 탄 다는 것 == 섬 개수 증가
                flag = False

                while queue:
                    pos = queue.popleft()

                    cnt = 0
                    for dx, dy in d:
                        x, y = pos[0] + dx, pos[1] + dy

                        if not 0 <= x < n or not 0 <= y < m:
                            continue

                        if not vis[x][y]:
                            if not board[x][y]:
                                cnt += 1
                            else:
                                queue.append((x, y))
                                vis[x][y] = True
                    board[pos[0]][pos[1]] = board[pos[0]][pos[1]] - cnt if board[pos[0]][pos[1]] > cnt else 0

        if landCnt >= 2:
            print(year - 1)
            quit()
    if flag:  # board를 전부 돌았을 때 한 번도 조건에 걸리지 않으면 break
        print(0)
        break
