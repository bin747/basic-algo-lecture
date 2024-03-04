from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

# 입력 받으면서 0과 2인 좌표 뽑아오고, 0 개수 뽑기
safe = []
virus = []
board = []
zero_cnt = 0
for i in range(n):
    sample = list(map(int, input().split()))
    for j in range(m):
        if sample[j] == 0:
            safe.append((i, j))
            zero_cnt += 1
        elif sample[j] == 2:
            virus.append((i, j))
    board.append(sample)

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(test_board):
    queue = deque()
    cnt = 0  # 바이러스 전파된 개수
    for i in virus:
        queue.append(i)
    while queue:
        pos = queue.popleft()
        for dx, dy in d:
            x = pos[0] + dx
            y = pos[1] + dy

            if not 0 <= x < n or not 0 <= y < m:
                continue
            if test_board[x][y] == 0:
                test_board[x][y] = 2
                cnt += 1
                queue.append((x, y))

    return zero_cnt - 3 - cnt  # 0개수 - 3(벽 개수) - 바이러스 전파 개수 == safe 공간


result = 0
# 0인 좌표 중 3개 뽑아서 벽 만들고, bfs 돌림
for points in combinations(safe, 3):
    test = copy.deepcopy(board)
    for i in range(3):
        test[points[i][0]][points[i][1]] = 1
    result = max(result, bfs(test))  # safe 공간 중 최대 값

print(result)
