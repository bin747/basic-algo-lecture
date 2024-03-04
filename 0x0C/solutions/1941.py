import sys
from collections import deque
from itertools import combinations

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

board = []
for _ in range(5):
    board.append(list(sys.stdin.readline().strip()))


def bfs(combi_list):
    """
    7가지 수가 이어져 있는지, Y의 개수가 최대 3개인지 체크

    Args:
        combi_list: 뽑혀진 7가지 숫자의 x좌표, y좌표, 방문여부

    Returns: 이어져있고 칠공주 가능 -> 1, 불가 -> 0
    """
    queue = deque()
    vis = [False for _ in range(7)]
    queue.append(combi_list[0])
    vis[0] = True
    cnt = [0, 0, 1]  # 'Y' 개수, 'S' 개수, 이어진 개수

    while queue:
        pos = queue.popleft()

        if board[pos[0]][pos[1]] == 'Y':
            cnt[0] += 1
        else:
            cnt[1] += 1

        if cnt[0] >= 4:
            return 0

        for dx, dy in d:
            x = pos[0] + dx
            y = pos[1] + dy

            if not 0 <= x < 5 or not 0 <= y < 5:
                continue

            if (x, y) in combi_list:
                index = combi_list.index((x, y))
                if not vis[index]:
                    vis[index] = True
                    cnt[2] += 1
                    queue.append((x, y))
    if cnt[2] != 7:
        return 0
    else:
        return 1


result = 0
# 좌표들 중 7개 뽑아서 bfs 돌림
for combi in combinations([(i, j) for i in range(5) for j in range(5)], 7):
    result += bfs(combi)

print(result)